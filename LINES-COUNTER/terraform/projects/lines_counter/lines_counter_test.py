import json
import boto3
import pymysql

def rds_tester():

    # Create a session using your AWS credentials
    session = boto3.Session(
        aws_access_key_id='',
        aws_secret_access_key='',
        region_name='us-east-1'
    )

    # Create an RDS client object
    rds_client = session.client('rds')

    # # Create an RDS client object
    # rds_client = boto3.client('rds')

    # Retrieve information about the RDS instances
    response = rds_client.describe_db_instances()

    # Extract the endpoint and credentials of the first RDS instance
    if 'DBInstances' in response and len(response['DBInstances']) > 0:
        endpoint = response['DBInstances'][0]['Endpoint']['Address']
        port = response['DBInstances'][0]['Endpoint']['Port']
        database_name = response['DBInstances'][0]['DBName']
        user_name = response['DBInstances'][0]['MasterUsername']
        user_password = '12345678'

        try:
            # Connect to the database using a MySQL client library
            connection = pymysql.connect(
                host=endpoint,
                port=port,
                user=user_name,
                passwd=user_password,
                database=database_name
            )
            print("Connection successful!")

            # Execute SQL queries
            cursor = connection.cursor()
            # Check if the table exists
            table_name = 'FilesLines'
            table_exists_query = f"SHOW TABLES LIKE '{table_name}'"
            cursor.execute(table_exists_query)
            table_exists = cursor.fetchone()

            if not table_exists:
                raise Exception("Table doesn't exist!")

            # Execute SQL query
            select_query = "SELECT * FROM FilesLines"
            cursor.execute(select_query)

            # Fetch all rows from the result set
            rows = cursor.fetchall()
            print(f"Number of entries in the table: {len(rows)}")
            # Print the data
            for row in rows:
                print(row)

            # Close the database connection
            cursor.close()
            connection.close()
            print("Connection closed!")

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    else:
        print("No RDS instances found.")


rds_tester()