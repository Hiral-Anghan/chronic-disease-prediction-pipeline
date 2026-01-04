                                   Chronic Disease Prediction Pipeline


This project implements an end-to-end data engineering and machine learning pipeline for predicting chronic (heart) disease.
The pipeline covers data ingestion, cleaning, modeling, evaluation, explainability, fairness analysis, and final persistence of results in a relational database.

The system is designed around four research questions (RQ1–RQ4) and is logically orchestrated using Apache Airflow DAGs, with all analytical logic implemented in modular Python scripts.


Dataset Links

Dataset Name: Heart Disease Dataset
Source: UCI Machine Learning Repository
Dataset Link:
https://archive.ics.uci.edu/ml/datasets/heart+disease

Research Questions

RQ1: How does data quality (missing values and noise) affect predictive model performance?

RQ2: How do different feature engineering techniques and machine learning models influence prediction accuracy?

RQ3: Which features contribute most to chronic disease predictions based on explainability methods?

RQ4: Are model predictions fair across demographic groups such as sex?


Pipeline Design Philosophy

This project follows a batch-oriented analytical pipeline design:

Raw CSV
   ↓
Data Ingestion
   ↓
Data Cleaning & Validation        (RQ1)
   ↓
Model Training & Evaluation       (RQ2)
   ↓
Explainability Analysis           (RQ3)
   ↓
Fairness & Ethics Analysis        (RQ4)
   ↓
FINAL DATA PERSISTENCE IN SQL     (MySQL)


How to Run the Code (Without Airflow)

1️⃣ Activate Virtual Environment
.venv\Scripts\activate

2️⃣ Run RQ1 – Data Preparation
python src/data_ingestion/ingest_data.py
python src/data_cleaning/clean_data.py

3️⃣ Run RQ2 – Model Training & Evaluation
python src/modeling/rq2_train_models.py
python src/evaluation/rq2_performance_tables.py
python src/evaluation/rq2_confusion_matrices.py
python src/evaluation/rq2_roc_curves.py
python src/evaluation/rq2_training_time_plot.py
python src/evaluation/rq2_interpretability_table.py

4️⃣ Run RQ3 – Explainability
python src/explainability/rq3_feature_importance.py
python src/explainability/rq3_shap_summary.py
python src/explainability/rq3_shap_local_explanation.py
python src/explainability/rq3_partial_dependence.py
python src/explainability/rq3_clinical_feature_table.py

5️⃣ Run RQ4 – Fairness & Ethics
python src/fairness/rq4_sex_fairness.py
python src/fairness/rq4_age_fairness.py
python src/fairness/rq4_sex_fairness_plot.py
python src/fairness/rq4_age_fairness_plot.py
python src/fairness/rq4_ethical_risk_summary.py

6️⃣ Final Step – Store Results in MySQL
python src/data_storage/store_final_data_sql.py

All figures and tables are generated automatically and saved to the figures/ and tables/ folders.


How to Run the Airflow DAG
Step 1: Start Airflow using Docker
docker-compose -f docker-compose.airflow-test.yaml up -d

Step 2: Open the Airflow web interface
http://localhost:8080

Step 3: Log in to Airflow
Username: admin  
Password: admin

Step 4: Locate the DAG and trigger the dag
On the right side of the DAG entry in the Airflow UI, click the play (▶) button to trigger the DAG execution.


Project Structure
chronic-disease-prediction-pipeline/
│
├── dags/ 
│   ├── rq1_pipeline_dag.py
│   ├── rq2_pipeline_dag.py
│   ├── rq3_explainability_dag.py
│   ├── rq4_fairness_dag.py                     
│
├── src/
│   ├── data_ingestion/
│   │      ├── ingest_data.py
│   ├── data_cleaning/
│   │      ├── clean_data.py
│   ├── modeling/
│   │      ├── rq1_model_comparison.py
│   │      ├── rq2_train_models.py
│   ├── evaluation/
│   │      ├── rq1_data_quality_analysis.py
│   │      ├── rq2_confusion_matrices.py
│   │      ├── rq2_interpretability_table.py
│   │      ├── rq2_model_evaluation.py
│   │      ├── rq2_performance_tables.py
│   │      ├── rq2_roc_curves.py
│   │      ├── rq2_training_time_plot.py
│   ├── explainability/
│   │      ├── rq3_clinical_feature_table.py
│   │      ├── rq3_feature_importance.py
│   │      ├── rq3_partial_dependence.py
│   │      ├── rq3_shap_local_explanation.py
│   │      ├── rq3_shap_summary.py
│   ├── fairness/
│   │      ├── rq4_age_fairness.py
│   │      ├── rq4_age_fairness_plot.py
│   │      ├── rq4_ethical_risk_summary.py
│   │      ├── rq4_prepare_subgroups.py
│   │      ├── rq4_sex_fairness.py
│   │      ├── rq4_sex_fairness_plot.py
│   └── data_storage/
│        ├── store_final_data_sql.py            
│
├── data/
│   ├── sample/
│   └── processed/
│
├── models/                       
├── figures/                     
├── tables/                       
│
├── docker-compose.airflow-test.yaml
├── requirements.txt
└── README.md

This project demonstrates a complete data engineering workflow, from raw data ingestion to ethical evaluation and final persistence of machine learning results.
It emphasizes modularity, reproducibility, and sound architectural decisions, making it suitable for both academic evaluation and real-world learning.