# Fraud Detection MLOps

## Project description
This project develops a machine learning model to detect fraudulent financial transactions using a dataset containing approximately 6.36 million transactions.

The analysis focuses on hyperparameter optimization, temporal evaluation, experiment tracking with MLflow, and model monitoring.

## Objectives
- Develop a fraud detection model using XGBoost.
- Optimize hyperparameters using RandomizedSearchCV.
- Evaluate model performance on a separate temporal production period.
- Track experiments and metrics with MLflow.
- Monitor data distribution changes and fraud prevalence.

## Repository structure
The repository includes notebooks for preprocessing, model training, interpretability, and monitoring, along with reports and project documentation.

## Main results
The original XGBoost model achieved an Average Precision (PR-AUC) of 0.9726 on the production evaluation period.

## Technologies
Python, pandas, Polars, scikit-learn, XGBoost, MLflow, and Jupyter Notebook.
