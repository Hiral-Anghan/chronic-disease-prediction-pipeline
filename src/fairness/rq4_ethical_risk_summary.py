from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="rq4_fairness_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["rq4", "fairness", "ethics"],
) as dag:

    sex_fairness = BashOperator(
        task_id="sex_fairness",
        bash_command="python /opt/airflow/src/fairness/rq4_sex_fairness.py",
    )

    age_fairness = BashOperator(
        task_id="age_fairness",
        bash_command="python /opt/airflow/src/fairness/rq4_age_fairness.py",
    )

    ethical_risk_summary = BashOperator(
        task_id="ethical_risk_summary",
        bash_command="python /opt/airflow/src/fairness/rq4_ethical_risk_summary.py",
    )

    store_final_sql = BashOperator(
        task_id="store_final_sql",
        bash_command="python /opt/airflow/src/data_storage/store_final_data_sql.py",
    )

    sex_fairness >> age_fairness >> ethical_risk_summary >> store_final_sql
