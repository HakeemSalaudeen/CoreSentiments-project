# import logging

# def fetch_pageviews(file_path, sql_file_name, company_names, table_name):
#         """
#         Generates SQL INSERT statements for specified company names from a text file.
#         Args:
#             file_name (str): The name of the input text file containing company data.
#             sql_file_name (str): The name of the output SQL file to write the INSERT statements.
#             company_names (list): A list of company names to filter for.
#             table_name (str): The name of the SQL table where data will be inserted.
#         """
        
# file_path = '/home/hakeem_bluechip/airflow/my_env/dags/CoreSentiments/LandingPath.zip'
# company_names = ['Amazon', 'Apple', 'Facebook', 'Google', 'Microsoft']
# #sql_file_name = 'C:/Users/hakee/Desktop/CDE/Airflow/CoreSentiments/CoreSentimentAssignment.py'
# #table_name = 'CoreSentiments'
# page_titles = []                                                     #lists to store the extracted columns
# page_views = []

# with open(file_path, 'r', encoding='utf-8') as file:                # Open the input file in read mode
#     for line in file:                                               # Read each line in the file
#         columns = line.split()                                      # Split the line by spaces          
#         if len(columns) >= 3:                                       # Check if there are enough columns
#             page_titles.append(columns[1])                           # Extract the second and third columns
#             page_views.append(columns[2])
            
#     for page_view in page_views:
#         target_folder = '/home/hakeem_bluechip/airflow/my_env/dags/CoreSentiments/includes/company.csv'
#         with open (target_folder, 'wb') as f:
#             f.write(page_view)
#         print (f'Download {image_url} successful to {target_folder}')

# # # Open the SQL file for writing
# # with open(sql_file_name, 'w', encoding='utf-8') as sql_file:
# #     for sec, thr in zip(page_title, page_view):                      # Iterate through the extracted columns
# #         if sec in company_names:                                     # Check if the company name is in the list
# #                                                                         # Create the INSERT INTO statement
# #             sql_statement = f"INSERT INTO {table_name} (company_name, views) VALUES ('{sec}', {thr});/n"
# #             sql_file.write(sql_statement)                            # Write the SQL statement to the file





    
#     logging.info (f"SQL statements written to {sql_file_name}")
#     #print(f"SQL statements written to {sql_file_name}")