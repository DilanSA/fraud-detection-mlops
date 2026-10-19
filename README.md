# Detección de transacciones fraudulentas con Machine Learning

## 1. Descripción del proyecto

Este proyecto desarrolla un modelo de Machine Learning para identificar transacciones financieras fraudulentas a partir de un conjunto de datos de aproximadamente 6,36 millones de transacciones. Se utiliza XGBoost para entrenar y evaluar modelos, optimizar hiperparámetros y analizar su rendimiento sobre un periodo temporal independiente.

El proyecto incorpora seguimiento de experimentos con MLflow, interpretación del modelo y análisis de cambios en la distribución de los datos.

## 2. Objetivos

- Desarrollar un modelo de clasificación para detectar transacciones fraudulentas.
- Optimizar los hiperparámetros mediante RandomizedSearchCV.
- Evaluar el rendimiento con métricas apropiadas para clases desbalanceadas.
- Interpretar la importancia de las variables predictoras.
- Analizar cambios en la distribución de los datos y en la prevalencia del fraude.
- Registrar experimentos y resultados con MLflow.

## 3. Fuente de datos

El conjunto de datos se obtuvo de Kaggle:

[Conjunto de datos de transacciones financieras para detección de fraude](https://www.kaggle.com/datasets/charlesbeauchamp/ps-20174392719-1491204439457-logcsv?resource=download)

- **Archivo:** `dataset_proyecto.csv`
- **Registros:** 6.362.620 transacciones.
- **Variables:** 11.
- **Variable objetivo:** `isFraud`.

La variable objetivo identifica si una transacción es fraudulenta. El conjunto presenta un fuerte desbalance entre transacciones legítimas y fraudulentas.

## 4. Flujo de trabajo

1. **Preprocesamiento:** preparación de los datos y transformación de variables categóricas.
2. **Entrenamiento:** ajuste de un modelo XGBoost inicial y optimización de hiperparámetros.
3. **Interpretabilidad:** análisis de la importancia de las variables.
4. **Evaluación y monitorización:** evaluación temporal del rendimiento y comparación de distribuciones entre periodos.

## 5. Estrategia de evaluación temporal

Los datos se separaron según la variable temporal `step`:

- **Referencia y entrenamiento:** `step <= 400`, con 5.787.030 transacciones.
- **Producción y evaluación:** `step >= 401`, con 575.590 transacciones.

El periodo de producción se mantuvo separado del entrenamiento y de la búsqueda de hiperparámetros para evaluar la capacidad de generalización temporal de los modelos.

## 6. Optimización de hiperparámetros

Se utilizó RandomizedSearchCV con seis configuraciones, validación cruzada estratificada de tres particiones y una muestra de 200.000 transacciones del periodo de entrenamiento.

La métrica utilizada para seleccionar la configuración fue Average Precision.

Los mejores hiperparámetros encontrados fueron:

- `n_estimators`: 150
- `max_depth`: 3
- `learning_rate`: 0.1
- `min_child_weight`: 5
- `subsample`: 1.0
- `colsample_bytree`: 1.0

El modelo optimizado se entrenó posteriormente con el conjunto completo de referencia.

## 7. Resultados de evaluación

Los modelos se evaluaron en el periodo de producción con un umbral de clasificación de 0,5.

| Métrica | XGBoost original | XGBoost optimizado |
|---|---:|---:|
| Average Precision (PR-AUC) | 0,9726 | 0,9516 |
| ROC-AUC | 0,9998 | 0,9996 |
| Precisión de fraude | 0,5714 | 0,2796 |
| Recall de fraude | 0,9971 | 0,9997 |
| Falsas alarmas | 2.794 | 9.621 |
| Fraudes no detectados | 11 | 1 |

El modelo original obtuvo mejores resultados en Average Precision y precisión de fraude, además de generar menos falsas alarmas. El optimizado alcanzó un recall ligeramente superior, a costa de incrementar las falsas alarmas.

Por estos resultados, se conserva el modelo original como modelo principal del proyecto.

## 8. Interpretabilidad

Se analizó la importancia de las variables del modelo XGBoost para identificar cuáles contribuyen más a sus predicciones. Los resultados se presentan en `reports/importancia_variables.png`.

La importancia del modelo describe su comportamiento predictivo y no debe interpretarse como evidencia de causalidad.

## 9. Monitorización

Se realizaron análisis retrospectivos para comparar los periodos de referencia y producción:

- Distancia de Wasserstein para comparar las distribuciones de seis variables numéricas.
- Comparación de la prevalencia del fraude entre periodos.
- Evaluación de métricas de clasificación en el periodo de producción.

La prevalencia del fraude aumentó de 0,0774 % en referencia a 0,6491 % en producción. Este cambio constituye una señal que requiere seguimiento, pero no demuestra por sí solo la existencia de concept drift ni un deterioro del modelo.

La monitorización implementada corresponde a un análisis retrospectivo; no constituye todavía un sistema automatizado de monitorización en tiempo real.

## 10. Seguimiento de experimentos

Se utilizó MLflow para registrar los parámetros de la búsqueda de hiperparámetros, las métricas de evaluación y los resultados de comparación entre modelos.

La base de datos local de MLflow y los archivos de experimentación no se incluyen directamente en el repositorio.

## 11. Estructura del repositorio

- `notebooks/`: cuadernos de preprocesamiento, entrenamiento, interpretabilidad y monitorización.
- `data/`: documentación y enlace de acceso al conjunto de datos.
- `models/`: modelos entrenados y preprocesador.
- `reports/`: métricas, gráficos e informe HTML de monitorización.
- `requirements.txt`: dependencias de Python.
- `.gitignore`: archivos excluidos del control de versiones.

## 12. Requisitos y reproducibilidad

Se requiere Python y las bibliotecas indicadas en `requirements.txt`. Para reproducir los análisis, descarga el conjunto de datos desde Kaggle y coloca `dataset_proyecto.csv` en el directorio `data/`.

Los notebooks deben ejecutarse siguiendo el orden numérico indicado en sus nombres.

## 13. Limitaciones

- La evaluación se realizó sobre un único periodo temporal de producción.
- La optimización se realizó sobre una muestra del conjunto de entrenamiento.
- El umbral de clasificación se fijó en 0,5 para comparar los modelos.
- Los análisis de distribución no constituyen por sí solos una detección concluyente de concept drift.
- La monitorización no está automatizada en tiempo real.

## 14. Tecnologías utilizadas

Python, pandas, Polars, NumPy, scikit-learn, XGBoost, SciPy, Matplotlib, Joblib, MLflow y Jupyter Notebook.
