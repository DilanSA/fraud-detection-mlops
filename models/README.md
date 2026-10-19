# Modelos entrenados

Esta carpeta está destinada a los modelos desarrollados para el proyecto de detección de transacciones fraudulentas.

## Modelos

- `xgboost_fraude.joblib`: modelo XGBoost original utilizado como referencia.
- `xgboost_fraude_optimizado.joblib`: modelo XGBoost entrenado con los mejores hiperparámetros obtenidos mediante RandomizedSearchCV.

## Selección del modelo

Ambos modelos se evaluaron sobre el periodo de producción definido por `step >= 401`. El modelo original obtuvo un mejor Average Precision (PR-AUC) y generó menos falsas alarmas, por lo que se conserva como modelo principal.

## Reproducibilidad

Los modelos pueden generarse ejecutando el notebook `02_entrenamiento.ipynb`, después de disponer del conjunto de datos y completar el preprocesamiento correspondiente.
