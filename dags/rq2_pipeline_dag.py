from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="rq2_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["rq2", "modeling"],
) as dag:

    train_models = BashOperator(
        task_id="train_models",
        bash_command="python /opt/airflow/src/modeling/rq2_model_training.py",
    )

    performance_tables = BashOperator(
        task_id="performance_tables",
        bash_command="python /opt/airflow/src/evaluation/rq2_performance_tables.py",
    )

    confusion_matrices = BashOperator(
        task_id="confusion_matrices",
        bash_command="python /opt/airflow/src/evaluation/rq2_confusion_matrices.py",
    )

    roc_curves = BashOperator(
        task_id="roc_curves",
        bash_command="python /opt/airflow/src/evaluation/rq2_roc_curves.py",
    )

    train_models >> performance_tables >> confusion_matrices >> roc_curves
