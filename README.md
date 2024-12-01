# Building a Data Pipeline with Apache Airflow

## Objective
This capstone project focuses on strengthening my understanding of Data Pipeline Orchestration using Apache Airflow. The primary goal is to design and implement a data pipeline that efficiently handles data ingestion, processing, storage, and analysis.

## Deliverables
The key deliverable for this project is a fully functional data pipeline orchestrated with Apache Airflow.

---

## Project Scenario

### Background
Imagine a data consulting organization aiming to develop a stock market prediction tool called *CoreSentiment*. This tool will utilize sentiment analysis to predict market trends. To achieve this, the organization plans to analyze the number of Wikipedia page views for specific companies as an indicator of public interest and sentiment.

The data source for this project is Wikipedia pageview data, which provides insights into how often specific company pages are viewed.

---

## Project Tasks

### Overview
To kickstart the project, I created an Apache Airflow Directed Acyclic Graph (DAG) that automates the process of pulling Wikipedia pageview data for a selected one-hour duration in October 2024. The focus was narrowed down to five major companies: Amazon, Apple, Facebook, Google, and Microsoft. This initial selection allows for hypothesis validation and ensures a manageable scope for analysis.

### Detailed Steps
1. **Data Download and Extraction**:
   Using the DAG, I automated the download of a zip file containing Wikipedia pageview data for a specific hour. The file was then extracted to access the raw data.

2. **Data Processing**:
   From the extracted data, I filtered out unnecessary fields and focused only on the relevant page names (companies) and their corresponding view counts.

3. **Data Storage**:
   The processed data was loaded into a CSV file

4. **Simple Analysis**:
   To derive insights, I performed a basic analysis to identify the company with the highest number of page views during the selected hour. This step provided a preliminary understanding of public interest trends.

---

## Results and Insights
The pipeline successfully orchestrated all tasks, from downloading and processing data to storing it in a CSV and performing analysis. The analysis revealed which of the five companies garnered the most attention during the specified hour.

This project not only reinforced my technical skills in Apache Airflow but also demonstrated the potential of integrating public data sources like Wikipedia into predictive models.

---

## Conclusion
By completing this project, I gained hands-on experience in building and orchestrating a data pipeline using Apache Airflow. The ability to automate data workflows and analyze results efficiently is critical in the world of data consulting and analytics. This project serves as a foundation for exploring more advanced use cases involving sentiment analysis and stock market predictions.

