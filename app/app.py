
from pathlib import Path

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent.parent
REPORTS = ROOT / "reports"

st.set_page_config(
    page_title="Monitorización de fraude",
    page_icon="📊",
    layout="wide",
)

st.title("Monitorización del modelo de detección de fraude")
st.caption("Evaluación retrospectiva de rendimiento y cambios en los datos.")

st.info(
    "Este panel presenta resultados históricos. "
    "No es un sistema de monitorización en tiempo real."
)


@st.cache_data
def cargar_csv(nombre):
    ruta = REPORTS / nombre
    if ruta.exists():
        return pd.read_csv(ruta)
    return None


# 1. Prevalencia del fraude
st.header("1. Prevalencia del fraude")

prevalencia = cargar_csv("prevalencia_fraude.csv")

if prevalencia is not None:
    columnas = {
        "Periodo": "Periodo",
        "Transacciones": "Total transacciones",
        "Fraudes": "Fraudes",
        "Prevalencia (%)": "Prevalencia_fraude_%"
    }

    if all(c in prevalencia.columns for c in columnas.values()):
        c1, c2 = st.columns(2)

        referencia = prevalencia[
            prevalencia["Periodo"] == "Referencia"
        ]
        produccion = prevalencia[
            prevalencia["Periodo"] == "Producción"
        ]

        if not referencia.empty and not produccion.empty:
            c1.metric(
                "Prevalencia en referencia",
                f'{referencia.iloc[0]["Prevalencia_fraude_%"]:.4f}%'
            )
            c2.metric(
                "Prevalencia en producción",
                f'{produccion.iloc[0]["Prevalencia_fraude_%"]:.4f}%'
            )

        st.dataframe(prevalencia, use_container_width=True)

        grafico = prevalencia.set_index("Periodo")[
            "Prevalencia_fraude_%"
        ]
        st.bar_chart(grafico)
    else:
        st.warning("Las columnas de prevalencia no tienen el formato esperado.")
else:
    st.warning("No se encontró reports/prevalencia_fraude.csv.")


# 2. Rendimiento del modelo
st.header("2. Métricas de evaluación en producción")

metricas = cargar_csv("metricas_produccion.csv")

if metricas is not None:
    st.dataframe(metricas, use_container_width=True)

    if not metricas.empty:
        fila = metricas.iloc[0]
        c1, c2, c3 = st.columns(3)

        c1.metric("Average Precision", f'{fila["average_precision"]:.4f}')
        c2.metric("ROC-AUC", f'{fila["roc_auc"]:.4f}')
        c3.metric("Recall de fraude", f'{fila["recall_fraude"]:.4f}')

        c4, c5, c6 = st.columns(3)
        c4.metric("Transacciones", f'{int(fila["registros"]):,}')
        c5.metric("Falsas alarmas", f'{int(fila["falsas_alarmas"]):,}')
        c6.metric("Fraudes no detectados", f'{int(fila["fraudes_no_detectados"]):,}')
else:
    st.warning("No se encontró reports/metricas_produccion.csv.")


# 3. Cambios en la distribución de los datos
st.header("3. Análisis de data drift")

drift = cargar_csv("data_drift_wasserstein.csv")

if drift is not None:
    st.dataframe(drift, use_container_width=True)

    columna_distancia = "Distancia Wasserstein"
    columna_variable = "Variable"

    if columna_distancia in drift.columns and columna_variable in drift.columns:
        grafico = drift.set_index(columna_variable)[columna_distancia]
        st.bar_chart(grafico)
        st.caption(
            "La distancia de Wasserstein cuantifica diferencias entre "
            "distribuciones. Su magnitud depende de la escala de cada variable."
        )
else:
    st.warning("No se encontró reports/data_drift_wasserstein.csv.")


# 4. Informe completo
st.header("4. Informe de monitorización")

informe = REPORTS / "informe_monitorizacion.html"

if informe.exists():
    st.success("El informe HTML está disponible en la carpeta reports.")
    st.caption("Archivo: reports/informe_monitorizacion.html")
else:
    st.warning("No se encontró reports/informe_monitorizacion.html.")

st.divider()
st.caption("Proyecto académico de detección de transacciones fraudulentas.")
