from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 0,
}

with DAG(
    dag_id="rq1_end_to_end_pipeline",
    default_args=default_args,
    description="RQ1: Impact of data quality on model performance",
    schedule_interval=None,
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    ingest_data = BashOperator(
        task_id="ingest_data",
        bash_command="python /opt/airflow/src/data_ingestion/ingest_data.py",
    )

    clean_data = BashOperator(
        task_id="clean_data",
        bash_command="python /opt/airflow/src/data_cleaning/clean_data.py",
    )

    data_quality_analysis = BashOperator(
        task_id="rq1_data_quality_analysis",
        bash_command="python /opt/airflow/src/evaluation/rq1_data_quality_analysis.py",
    )

    model_comparison = BashOperator(
        task_id="rq1_model_comparison",
        bash_command="python /opt/airflow/src/modeling/rq1_model_comparison.py",
    )

    ingest_data >> clean_data >> data_quality_analysis >> model_comparison
