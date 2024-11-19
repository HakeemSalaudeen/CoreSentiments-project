import logging
import csv

def fetch_pageviews(file_path, csv_file_path, company_names):
    """
    Generates a CSV file for specified company names from a text file.
    Args:
        file_path (str): The path of the input text file containing company data.
        csv_file_name (str): The name of the output CSV file to write the data.
        company_names (list): A list of company names to filter for.
    """
    
    page_title = []  # List to store the extracted company names
    page_view = []   # List to store the extracted page views

    with open(file_path, 'r', encoding='utf-8') as file:  # Open the input file in read mode
        for line in file:                                   # Read each line in the file
            columns = line.split()                          # Split the line by spaces          
            if len(columns) >= 3:                           # Check if there are enough columns
                page_title.append(columns[1])               # Extract the second column (company name)
                page_view.append(columns[2])                # Extract the third column (views)

    # Open the CSV file for writing
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)                   # Create a CSV writer object
        csv_writer.writerow(['Company Name', 'Page Views']) # Write the header row

        for sec, thr in zip(page_title, page_view):         # Iterate through the extracted columns
            if sec in company_names:                         # Check if the company name is in the list
                csv_writer.writerow([sec, thr])             # Write the company name and views to the CSV

    logging.info(f"CSV file written to {csv_file_path}")
    # print(f"CSV file written to {csv_file_name}")

# Example usage
# file_path = '/home/hakeem_bluechip/airflow/my_env/dags/CoreSentiments/LandingPath3.gz'
# company_names = ['Amazon', 'Apple', 'Facebook', 'Google', 'Microsoft']
# csv_file_path = '/home/hakeem_bluechip/airflow/my_env/dags/CoreSentiments/includes/company.csv'

# fetch_pageviews(file_path, csv_file_path, company_names)
