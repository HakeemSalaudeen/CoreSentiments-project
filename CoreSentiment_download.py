## Step 1 : Import module/operators 
#import airflow 
import requests, zipfile
from airflow import DAG 
from airflow.utils.dates import datetime
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from CoreSentiments.includes.download_zipped_file import download_zipped_file
from CoreSentiments.includes.fetch_pageviews_tocsv import fetch_pageviews
#import file 

# step 2  #Instantiate a DAG object;                                # this is the starting point of any workflow
with DAG(
    dag_id= "CoreSentiment_d1",                                        #name of the DAG
    start_date= datetime(2024, 10, 13),                             #The date at which the DAG should first start running
    schedule_interval=None,                                         #At what interval the DAG should run
    catchup=False,
    #tag="Assignment"
) as dag:
    

    # Step 4: Python operator for the function           
    download_zipped_files = PythonOperator(
        task_id='download_zipped_files',
        python_callable=download_zipped_file,
        op_kwargs={
            'url': 'https://dumps.wikimedia.org/other/pageviews/2024/2024-10/pageviews-20241020-230000.gz',
            'save_path': '/home/hakeem_bluechip/airflow/my_env/dags/CoreSentiments/LandingPath3.gz'
        } 
    )
    
    # step 5 : Task to extract the zip file
    extract_zip_files = BashOperator(
        task_id= 'extract_zip_files',
        bash_command = 'gunzip /home/hakeem_bluechip/airflow/my_env/dags/CoreSentiments/LandingPath3.gz' 
    )

    # Step 7: Python operator for fetching pageviews
    fetchPageviews = PythonOperator(
        task_id='fetchPageviews',
        python_callable= fetch_pageviews, 
        op_kwargs={
            'file_path' : '/home/hakeem_bluechip/airflow/my_env/dags/CoreSentiments/LandingPath3',
            'company_names' : ['Amazon', 'Apple', 'Facebook', 'Google', 'Microsoft'],
            'csv_file_path' : '/home/hakeem_bluechip/airflow/my_env/dags/CoreSentiments/includes/company.csv'
        }
    )
    
    # # Step 8: Database operator to load data (example for Postgres)
    # postgres_data_load = PostgresOperator(
    # task_id='postgres_data_load',
    # postgres_conn_id = '' #id of the connection you defined in the web server 
    # sql = '' #the relative path to the sql file containing the query 
    # )
    
    # Step 9: Set task dependencies
    download_zipped_files >> extract_zip_files >> fetchPageviews
