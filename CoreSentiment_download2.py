## Step 1 : Import module/operators
# import airflow
import requests
from airflow import DAG
from airflow.utils.dates import datetime
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import logging

# step 2  #Instantiate a DAG object;                                # this is the starting point of any workflow
with DAG(
    dag_id="CoreSentiment_d2",  # name of the DAG
    start_date=datetime(
        2024, 10, 13
    ),  # The date at which the DAG should first start running
    schedule_interval=None,  # At what interval the DAG should run
    catchup=False,
    # tag="Assignment"
) as dag:
    # Step 3: Python function to download a zip file
    def _download_zipped_file(url, save_path):
        # Note: You don't need to reassign these parameters since they'll be passed through op_kwargs
        zipped_files = requests.get(url)
        # Use the save_path parameter directly, not as a string
        with open(save_path, "wb") as f:
            f.write(zipped_files.content)
        print(f"File downloaded successfully and saved to: {save_path}")
        logging.info(f"File downloaded successfully and saved to: {save_path}")

    # Step 4: Python operator for the function
    download_zipped_files = PythonOperator(
        task_id="download_zipped_files",
        python_callable=_download_zipped_file,
        op_kwargs={
            "url": "https://dumps.wikimedia.org/other/pageviews/2024/2024-10/pageviews-20241012-230000.gz",
            "save_path": "/home/**/airflow/my_env/dags/CoreSentiments/LandingPath2.gz",
        },
    )

    # step 5 : Task to extract the zip file
    extract_zip_files = BashOperator(
        task_id="extract_zip_files",
        bash_command="gunzip /home/**/airflow/my_env/dags/CoreSentiments/LandingPath2.gz",
    )

    download_zipped_files >> extract_zip_files
