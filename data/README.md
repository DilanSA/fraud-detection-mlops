# Datos del proyecto

## Fuente de datos

El conjunto de datos utilizado en este proyecto contiene aproximadamente 6,36 millones de transacciones financieras y 11 variables, incluida la etiqueta que identifica las transacciones fraudulentas.

- **Nombre del archivo:** `dataset_proyecto.csv`
- **Variable objetivo:** `isFraud`
- **Número de registros:** 6.362.620
- **Número de variables:** 11
- **Fuente:** [Kaggle — Conjunto de datos de transacciones financieras para detección de fraude](https://www.kaggle.com/datasets/charlesbeauchamp/ps-20174392719-1491204439457-logcsv?resource=download)

## Acceso a los datos

El archivo original puede obtenerse desde el enlace de Kaggle indicado anteriormente. Para reproducir los análisis, descarga el conjunto de datos y coloca el archivo `dataset_proyecto.csv` en este directorio.

## Consideraciones

El archivo completo no se incluye directamente en este repositorio debido a su tamaño. Los notebooks utilizan este conjunto de datos para el preprocesamiento, entrenamiento, optimización de hiperparámetros, interpretabilidad y monitorización del modelo.

## Diccionario de datos

| Variable | Descripción | Función en el proyecto |
|---|---|---|
| `step` | Índice temporal de la transacción, expresado en unidades de tiempo del conjunto de datos. | Variable predictora y criterio de separación temporal. |
| `type` | Tipo de transacción financiera. | Variable predictora categórica. |
| `amount` | Importe de la transacción. | Variable predictora numérica. |
| `nameOrig` | Identificador de la cuenta de origen. | Excluida del modelo por ser un identificador. |
| `oldbalanceOrg` | Saldo de la cuenta de origen antes de la transacción. | Variable predictora numérica. |
| `newbalanceOrig` | Saldo de la cuenta de origen después de la transacción. | Variable predictora numérica. |
| `nameDest` | Identificador de la cuenta de destino. | Excluida del modelo por ser un identificador. |
| `oldbalanceDest` | Saldo de la cuenta de destino antes de la transacción. | Variable predictora numérica. |
| `newbalanceDest` | Saldo de la cuenta de destino después de la transacción. | Variable predictora numérica. |
| `isFraud` | Indica si la transacción está etiquetada como fraudulenta. | Variable objetivo. |
| `isFlaggedFraud` | Indicador del conjunto de datos que señala determinadas transacciones de tipo transferencia identificadas como sospechosas. | Excluida del modelo para evitar utilizar una señal preexistente del sistema. |

## Variables utilizadas por el modelo

Se utilizaron siete variables predictoras: `step`, `type`, `amount`, `oldbalanceOrg`, `newbalanceOrig`, `oldbalanceDest` y `newbalanceDest`.

La variable objetivo fue `isFraud`. Los identificadores `nameOrig` y `nameDest`, así como `isFlaggedFraud`, se excluyeron del entrenamiento.

El preprocesamiento incluyó la codificación de la variable categórica `type`.
