import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Load data from S3
job_postings = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://linkedin-jobs-raw/linkedin_job_postings.csv"]},
    format="csv",
    format_options={"withHeader": True}
)

job_skills = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://linkedin-jobs-raw/job_skills.csv"]},
    format="csv",
    format_options={"withHeader": True}
)

job_summary = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://linkedin-jobs-raw/job_summary.csv"]},
    format="csv",
    format_options={"withHeader": True}
)

# Data transformation and cleansing for job_postings
job_postings_cleaned = ApplyMapping.apply(
    frame=job_postings,
    mappings=[
        ("job_link", "string", "job_link", "string"),
        ("last_processed_time", "string", "last_processed_time", "string"),
        ("got_summary", "string", "got_summary", "string"),
        ("got_ner", "string", "got_ner", "string"),
        ("is_being_worked", "string", "is_being_worked", "string"),
        ("job_title", "string", "job_title", "string"),
        ("company", "string", "company", "string"),
        ("job_location", "string", "job_location", "string"),
        ("first_seen", "string", "first_seen", "string"),
        ("search_city", "string", "search_city", "string"),
        ("search_country", "string", "search_country", "string"),
        ("search_position", "string", "search_position", "string"),
        ("job_level", "string", "job_level", "string"),
        ("job_type", "string", "job_type", "string")
    ]
)

# Data transformation and cleansing for job_skills
job_skills_cleaned = ApplyMapping.apply(
    frame=job_skills,
    mappings=[
        ("job_link", "string", "job_link", "string"),
        ("job_skills", "string", "job_skills", "string")
    ]
)

# Data transformation and cleansing for job_summary
job_summary_cleaned = ApplyMapping.apply(
    frame=job_summary,
    mappings=[
        ("job_link", "string", "job_link", "string"),
        ("job_summary", "string", "job_summary", "string")
    ]
)

# Save cleaned data to Glue tables
glueContext.write_dynamic_frame.from_catalog(
    frame=job_postings_cleaned,
    database="linkedin_jobs_db",
    table_name="tbl_linkedin_job_postings"
)

glueContext.write_dynamic_frame.from_catalog(
    frame=job_skills_cleaned,
    database="linkedin_jobs_db",
    table_name="tbl_job_skills"
)

glueContext.write_dynamic_frame.from_catalog(
    frame=job_summary_cleaned,
    database="linkedin_jobs_db",
    table_name="tbl_job_summary"
)

job.commit()
