# Career Trends Analytics Engine

## Overview
The **Career Trends Analytics Engine** project aims to design and implement a scalable data engineering platform using AWS services. This platform will efficiently handle large datasets sourced from LinkedIn Jobs, focusing on the following key components:
- Data Ingestion
- Data Storage
- Data Processing
- Data Aggregation
- Data Visualization

## Components
### Data Ingestion
- **AWS Services:** AWS S3, AWS Glue
- **Description:** Efficiently ingest large CSV files into the platform. AWS S3 is used for initial storage, and AWS Glue is used for ETL (Extract, Transform, Load) processes.

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

## Repository Structure
- `etl/`: Con
