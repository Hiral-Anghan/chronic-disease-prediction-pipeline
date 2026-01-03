from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 0,
}

with DAG(
    dag_id="rq4_fairness_pipeline",
    default_args=default_args,
    description="RQ4: Fairness analysis and ethical risk assessment",
    schedule_interval=None,
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    # ----- Fairness Tables -----
    sex_fairness_table = BashOperator(
        task_id="sex_fairness_table",
        bash_command="python /opt/airflow/src/fairness/rq4_sex_fairness.py",
    )

    age_fairness_table = BashOperator(
        task_id="age_fairness_table",
        bash_command="python /opt/airflow/src/fairness/rq4_age_fairness.py",
    )

    # ----- Fairness Plots -----
    sex_fairness_plot = BashOperator(
        task_id="sex_fairness_plot",
        bash_command="python /opt/airflow/src/fairness/rq4_sex_fairness_plot.py",
    )

    age_fairness_plot = BashOperator(
        task_id="age_fairness_plot",
        bash_command="python /opt/airflow/src/fairness/rq4_age_fairness_plot.py",
    )

    # ----- Ethical Risk Summary -----
    ethical_risk_summary = BashOperator(
        task_id="ethical_risk_summary",
        bash_command="python /opt/airflow/src/fairness/rq4_ethical_risk_summary.py",
    )

    store_final_data = BashOperator(
    task_id="store_final_data_sql",
    bash_command="python /opt/airflow/src/data_storage/store_final_data_sql.py",
)



    # ----- Dependencies -----
    sex_fairness_table >> sex_fairness_plot
    age_fairness_table >> age_fairness_plot
    [sex_fairness_plot, age_fairness_plot] >> ethical_risk_summary
    ethical_risk_summary >> store_final_data
