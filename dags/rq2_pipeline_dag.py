from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 0,
}

with DAG(
    dag_id="rq2_model_comparison_pipeline",
    default_args=default_args,
    description="RQ2: Model performance vs interpretability",
    schedule_interval=None,
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    train_models = BashOperator(
        task_id="train_models",
        bash_command="python /opt/airflow/src/modeling/rq2_model_training.py",
    )

    evaluate_models = BashOperator(
        task_id="evaluate_models",
        bash_command="python /opt/airflow/src/evaluation/rq2_model_evaluation.py",
    )

    train_models >> evaluate_models
