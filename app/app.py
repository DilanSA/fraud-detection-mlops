from pathlib import Path

import pandas as pd
import streamlit as st

# Rutas de los reportes del repositorio
ROOT = Path(__file__).resolve().parent.parent
REPORTS = ROOT / "reports"

st.set_page_config(
    page_title="Monitorización de fraude",
    page_icon="📊",
    layout="wide",
)

st.title("Monitorización del modelo de detección de fraude")
st.caption(
    "Análisis retrospectivo de rendimiento, prevalencia del fraude "
    "y cambios en la distribución de los datos."
)

st.info(
    "Esta aplicación presenta resultados históricos. "
    "No constituye un sistema de monitorización en tiempo real."
)


def cargar_csv(nombre):
    ruta = REPORTS / nombre
    if ruta.exists():
        return pd.read_csv(ruta)
    return None


# 1. Prevalencia del fraude
st.header("1. Prevalencia del fraude")
prevalencia = cargar_csv("prevalencia_fraude.csv")

if prevalencia is not None:
    st.dataframe(prevalencia, use_container_width=True)

    # Mostrar gráficos si el archivo contiene columnas numéricas adecuadas
    numericas = prevalencia.select_dtypes(include="number").columns.tolist()
    if numericas:
        st.bar_chart(prevalencia.set_index(prevalencia.columns[0])[numericas])
else:
    st.warning("No se encontró prevalencia_fraude.csv en reports/.")


# 2. Métricas de producción
st.header("2. Métricas de evaluación")
metricas = cargar_csv("metricas_produccion.csv")

if metricas is not None:
    st.dataframe(metricas, use_container_width=True)
else:
    st.warning("No se encontró metricas_produccion.csv en reports/.")


# 3. Análisis de data drift
st.header("3. Cambios en la distribución de los datos")
drift = cargar_csv("data_drift_wasserstein.csv")

if drift is not None:
    st.dataframe(drift, use_container_width=True)

    numericas = drift.select_dtypes(include="number").columns.tolist()
    if numericas:
        st.bar_chart(drift.set_index(drift.columns[0])[numericas])
else:
    st.warning("No se encontró data_drift_wasserstein.csv en reports/.")


# 4. Informe HTML
st.header("4. Informe completo")

informe = REPORTS / "informe_monitorizacion.html"

if informe.exists():
    st.success(
        "El informe HTML está disponible en la carpeta reports/ "
        "del repositorio."
    )
    st.caption("Archivo: reports/informe_monitorizacion.html")
else:
    st.warning("No se encontró informe_monitorizacion.html en reports/.")


st.divider()
st.caption("Proyecto académico de detección de transacciones fraudulentas.")
