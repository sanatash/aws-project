import json
import boto3
import pymysql

import string
import random
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def lambda_handler(event, context):

    # Create a session using your AWS credentials
    session = boto3.Session(
        aws_access_key_id='',
        aws_secret_access_key='',
        region_name='us-east-1'
    )

    s3 = session.client('s3')
    bucket_name = str(event["Records"][0]["s3"]["bucket"]["name"])
    key_name = str(event["Records"][0]["s3"]["object"]["key"])
    obj = s3.get_object(Bucket=bucket_name, Key=key_name)
    body_len = len(obj['Body'].read().decode('utf-8').split("\n"))
    print(f"Bucket_name: {bucket_name}, key_name: {key_name}, body_len: {body_len} ")

    # Create an RDS client object
    rds_client = session.client('rds')

    # Retrieve information about the RDS instances
    response = rds_client.describe_db_instances()

    # Extract the endpoint and credentials of the first RDS instance
    if 'DBInstances' in response and len(response['DBInstances']) > 0:
        endpoint = response['DBInstances'][0]['Endpoint']['Address']
        port = response['DBInstances'][0]['Endpoint']['Port']
        database_name = response['DBInstances'][0]['DBName']
        user_name = response['DBInstances'][0]['MasterUsername']
        user_password = '12345678'
        print(f"RDS Endpoint: {endpoint}:{port}")
        print(f"RDS user: {user_name}")
        print(f"RDS user: {database_name}")

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
                # Create the table
                create_table_query = '''
CREATE TABLE FilesLines 
(ID VARCHAR(255) PRIMARY KEY, 
ObjectPath VARCHAR(255), 
Date DATETIME DEFAULT CURRENT_TIMESTAMP, 
AmountOfLines INT)
'''
                cursor.execute(create_table_query)
                connection.commit()
                print("Table created successfully!")

            else:
                print("Table already exist !!!")

            # Insert data into the table
            try:
                insert_query = "INSERT INTO FilesLines (ID, ObjectPath, AmountOfLines) VALUES (%s, %s, %s)"
                data = (id_generator(), key_name, body_len)
                cursor.execute(insert_query, data)
                connection.commit()
                print("Data inserted successfully!")
            except Exception as e:
                print(f"Error inserting data: {str(e)}")
                connection.rollback()

            # Execute SQL query
            select_query = "SELECT * FROM FilesLines"
            cursor.execute(select_query)

            # Fetch all rows from the result set
            rows = cursor.fetchall()

            # Print the data
            for row in rows:
                print(row)

            # Close the database connection
            cursor.close()
            connection.close()
            print("Connection closed!")

            return {
                'statusCode': 200,
                'body': 'Success'
            }
        except Exception as e:
            print(f"An error occurred: {str(e)}")

            return {
                'statusCode': 500,
                'body': 'Error'
            }
    else:
        print("No RDS instances found.")


    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

event = {
    "Records": [
        {
            "s3": {
                "bucket": {
                    "name": "lines-counter-app-s3-bucket"
                },
                "object": {
                    "key": "three_lines_file.txt"
                }
            }
        }
    ]
}

lambda_handler(event, '1')