# Career Trends Analytics Engine

## Overview
The **Career Trends Analytics Engine** project aims to design and implement a scalable data engineering platform using AWS services. This platform will efficiently handle large datasets sourced from LinkedIn Jobs, focusing on the following key components:
- Data Ingestion
- Data Storage
- Data Processing
- Data Aggregation
- Data Visualization

## Architecture Diagram
Below is the high-level architecture diagram of the data engineering platform:

![Architecture Diagram](https://github.com/g23ai1049/Data_Engineering_Repo/blob/main/Design_Diagram.jpg)

## Components
### Data Ingestion
- **AWS Services:** AWS S3, AWS Kinesis Data Streams, AWS Kinesis Firehose
- **Description:** Efficiently ingest large CSV files into the platform. AWS S3 is used for initial storage, and AWS Kinesis Data Streams and Firehose are used for streaming data to S3.

### Data Storage
- **AWS Services:** Amazon S3
- **Description:** Store raw and processed data securely and accessibly. Amazon S3 provides a robust storage solution that handles large datasets and integrates with other AWS services.

### Data Processing
- **AWS Services:** AWS Glue, AWS Lambda
- **Description:** Clean, transform, and prepare data for analysis. AWS Glue offers a fully managed ETL service, and AWS Lambda is used for serverless data processing tasks.

### Data Aggregation
- **AWS Services:** AWS Glue, Amazon Athena
- **Description:** Aggregate data to facilitate efficient querying and analysis. AWS Glue performs necessary transformations and aggregations, while Amazon Athena provides a serverless interactive query service.

### Data Visualization
- **AWS Services:** Amazon QuickSight
- **Description:** Create interactive dashboards and visualizations to derive insights from the data. Amazon QuickSight integrates seamlessly with Athena and S3.

## About the Dataset
LinkedIn is a widely used professional networking platform that hosts millions of job postings. This dataset contains 1.3 million job listings scraped from LinkedIn in the year 2024. The dataset can be used for various research tasks such as job market analysis, skills mapping, job recommendation systems, and more.

### Dataset Structure
1. **linkedin_job_postings.csv**
    - **Columns:**
        - `job_link`
        - `last_processed_time`
        - `got_summary`
        - `got_ner`
        - `is_being_worked`
        - `job_title`
        - `company`
        - `job_location`
        - `first_seen`
        - `search_city`
        - `search_country`
        - `search_position`
        - `job_level`
        - `job_type`

2. **job_skills.csv**
    - **Columns:**
        - `job_link`
        - `job_skills`

3. **job_summary.csv**
    - **Columns:**
        - `job_link`
        - `job_summary`

## Data Ingestion

### Step 1: Create an S3 Bucket
Create an S3 bucket to store raw data.

### Step 2: Create a Kinesis Data Stream
Create a Kinesis Data Stream to handle data ingestion.

### Step 3: Create a Kinesis Firehose Delivery Stream
Create a Kinesis Firehose Delivery Stream to deliver data from Kinesis Data Stream to Amazon S3.

### Step 4: Set Up Data Producers
Use the provided Python script to send data from CSV files to the Kinesis Data Stream.

#### Python Script
```python
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
