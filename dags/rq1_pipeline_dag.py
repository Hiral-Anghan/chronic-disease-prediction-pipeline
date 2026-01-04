from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="rq1_end_to_end_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["rq1", "data-quality"],
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
        task_id="data_quality_analysis",
        bash_command="python /opt/airflow/src/evaluation/rq1_data_quality_analysis.py",
    )

    model_comparison = BashOperator(
        task_id="model_comparison",
        bash_command="python /opt/airflow/src/modeling/rq1_model_comparison.py",
    )

    ingest_data >> clean_data >> data_quality_analysis >> model_comparison
