from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 0,
}

with DAG(
    dag_id="rq3_explainability_pipeline",
    default_args=default_args,
    description="RQ3: Explainability and trust analysis",
    schedule_interval=None,
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    f6 = BashOperator(
        task_id="feature_importance",
        bash_command="python /opt/airflow/src/explainability/rq3_feature_importance.py",
    )

    f7 = BashOperator(
        task_id="shap_summary",
        bash_command="python /opt/airflow/src/explainability/rq3_shap_summary.py",
    )

    t7 = BashOperator(
        task_id="clinical_table",
        bash_command="python /opt/airflow/src/explainability/rq3_clinical_feature_table.py",
    )

    f8 = BashOperator(
        task_id="shap_local",
        bash_command="python /opt/airflow/src/explainability/rq3_shap_local_explanation.py",
    )

    f9 = BashOperator(
        task_id="partial_dependence",
        bash_command="python /opt/airflow/src/explainability/rq3_partial_dependence.py",
    )

    f6 >> f7 >> t7 >> f8 >> f9
