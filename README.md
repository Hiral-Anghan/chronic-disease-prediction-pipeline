🫀 Chronic Disease Prediction Pipeline

End-to-End Data Engineering & Machine Learning Project

📌 Project Overview

This project implements an end-to-end data engineering and machine learning pipeline for predicting chronic (heart) disease.
The pipeline covers data ingestion, cleaning, modeling, evaluation, explainability, fairness analysis, and final persistence of results in a relational database.

The system is designed around four research questions (RQ1–RQ4) and is logically orchestrated using Apache Airflow DAGs, with all analytical logic implemented in modular Python scripts.

🎯 Research Questions
RQ1 – Data Quality

How does data quality impact model performance?

Data ingestion from CSV

Data cleaning and preprocessing

Data quality checks

Preparation for downstream modeling

RQ2 – Model Comparison

Which machine learning models provide the best performance–interpretability trade-off?

Logistic Regression

Random Forest

Performance metrics (Accuracy, F1-score)

Confusion matrices

ROC curves

Training time comparison

Interpretability comparison table

RQ3 – Explainability

How can explainability methods improve trust in predictions?

Feature importance analysis

SHAP global explanations

SHAP local explanations

Partial dependence plots

Clinical feature interpretation table

RQ4 – Fairness & Ethics

Are there performance disparities across demographic groups?

Performance by sex

Performance by age groups

Fairness comparison tables

Ethical risk summary diagram

🏗️ Project Structure
chronic-disease-prediction-pipeline/
│
├── dags/                         # Airflow DAG definitions (RQ1–RQ4)
│
├── src/
│   ├── data_ingestion/
│   ├── data_cleaning/
│   ├── modeling/
│   ├── evaluation/
│   ├── explainability/
│   ├── fairness/
│   └── data_storage/             # Final SQL persistence
│
├── data/
│   ├── sample/
│   └── processed/
│
├── models/                       # Trained models
├── figures/                      # Generated figures
├── tables/                       # Generated tables
│
├── docker-compose.yaml
├── requirements.txt
└── README.md

⚙️ Technologies Used

Python 3.8+

Pandas, NumPy

Scikit-learn

SHAP

Matplotlib

SQLAlchemy

MySQL 8.0

Apache Airflow 2.8.1

Docker & Docker Compose

🔁 Pipeline Design Philosophy

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

Key Design Decision

Data is stored in SQL only at the final stage

The database acts as a curated analytical store

Intermediate steps operate on CSVs for flexibility and speed

This design is appropriate for offline research and experimentation workflows.

🗄️ Final Data Persistence (MySQL)

At the end of the pipeline, a final curated dataset is stored in MySQL, including:

Cleaned features

Model predictions

Demographically relevant attributes

Table Created
final_heart_disease_analytics

Persistence Behavior

Implemented using if_exists="replace"

Each pipeline run replaces the table

Ensures the database always reflects the latest validated results

This makes the persistence step idempotent and reproducible.

▶️ How to Run the Project
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

📊 Outputs Generated
📁 Tables

RQ2 performance tables

RQ3 explainability tables

RQ4 fairness comparison tables

📁 Figures

Confusion matrices

ROC curves

SHAP plots

Partial dependence plots

Fairness comparison charts

Ethical risk summary diagram

All outputs are automatically generated and reproducible.

🌬️ Airflow DAGs

Airflow DAGs are provided to represent the logical orchestration of the pipeline:

DAG	Description
rq1_pipeline_dag.py	Data ingestion and cleaning
rq2_pipeline_dag.py	Model training and evaluation
rq3_explainability_dag.py	Explainability analysis
rq4_fairness_dag.py	Fairness analysis and final persistence

Due to local Windows + Docker limitations, DAG execution was not fully enforced.
All scripts were executed and validated independently.

🧠 Key Learning Outcomes

End-to-end ML pipeline design

Data quality and preprocessing

Model comparison and evaluation

Explainability with SHAP

Fairness analysis across demographics

SQL persistence using MySQL

Airflow DAG design and debugging

Dependency and environment management

✅ Conclusion

This project demonstrates a complete data engineering workflow, from raw data ingestion to ethical evaluation and final persistence of machine learning results.
It emphasizes modularity, reproducibility, and sound architectural decisions, making it suitable for both academic evaluation and real-world learning.