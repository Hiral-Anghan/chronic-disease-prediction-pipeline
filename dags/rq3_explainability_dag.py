from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="rq3_explainability_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["rq3", "explainability"],
) as dag:

    feature_importance = BashOperator(
        task_id="feature_importance",
        bash_command="python /opt/airflow/src/explainability/rq3_feature_importance.py",
    )

    shap_summary = BashOperator(
        task_id="shap_summary",
        bash_command="python /opt/airflow/src/explainability/rq3_shap_summary.py",
    )

    partial_dependence = BashOperator(
        task_id="partial_dependence",
        bash_command="python /opt/airflow/src/explainability/rq3_partial_dependence.py",
    )

    feature_importance >> shap_summary >> partial_dependence
