import boto3
import csv
import json
import time

# Initializing the Kinesis client
kinesis_client = boto3.client('kinesis', region_name='ap-south-1')

def send_data_to_kinesis(file_path, stream_name):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            kinesis_client.put_record(
                StreamName=stream_name,
                Data=json.dumps(row),
                PartitionKey="partitionkey"
            )
            print(f"Sent record to Kinesis: {row}")
            time.sleep(0.1)  

# List of CSV file paths
csv_files = [
    'linkedin_job_postings.csv',
    'job_skills.csv',
    'job_summary.csv'
]

# Sending data from each CSV file to the Kinesis stream
for csv_file in csv_files:
    send_data_to_kinesis(csv_file, 'linkedin-job-stream')
