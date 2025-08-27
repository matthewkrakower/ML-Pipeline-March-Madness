from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="ml_pipeline_simple",
    description="Run ML pipeline scripts in order",
    default_args=default_args,
    start_date=datetime(2025, 8, 1),
    schedule_interval=None,   
    catchup=False,
    tags=["ml", "pipeline"],
) as dag:

    preprocess_train = BashOperator(
        task_id="preprocess_train",
        bash_command="python scripts/preprocess_training.py"
    )

    train = BashOperator(
        task_id="train",
        bash_command="python scripts/train.py"
    )

    preprocess_test = BashOperator(
        task_id="preprocess_test",
        bash_command="python scripts/preprocess_test.py"
    )

    predict = BashOperator(
        task_id="predict",
        bash_command="python scripts/predict.py"
    )

    preprocess_train >> train >> preprocess_test >> predict