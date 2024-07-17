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

# Load data from the Glue Data Catalog
job_postings = glueContext.create_dynamic_frame.from_catalog(
    database="linkedin_jobs_db",
    table_name="tbl_linkedin_job_postings"
)

job_skills = glueContext.create_dynamic_frame.from_catalog(
    database="linkedin_jobs_db",
    table_name="tbl_job_skills"
)

job_summary = glueContext.create_dynamic_frame.from_catalog(
    database="linkedin_jobs_db",
    table_name="tbl_job_summary"
)

# Data transformation and cleansing for job_postings
job_postings_cleaned = ApplyMapping.apply(
    frame=job_postings,
    mappings=[
        ("job_link", "string", "job_link", "string"),
        ("last_processed_time", "string", "last_processed_time", "timestamp"),
        ("got_summary", "string", "got_summary", "string"),
        ("got_ner", "string", "got_ner", "string"),
        ("is_being_worked", "string", "is_being_worked", "string"),
        ("job_title", "string", "job_title", "string"),
        ("company", "string", "company", "string"),
        ("job_location", "string", "job_location", "string"),
        ("first_seen", "string", "first_seen", "timestamp"),
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

# Join the data
joined_data = Join.apply(
    job_postings_cleaned,
    job_skills_cleaned,
    'job_link',
    'job_link'
)

joined_data = Join.apply(
    joined_data,
    job_summary_cleaned,
    'job_link',
    'job_link'
)

# Cleaned and transformed data 
def transform_skills(dynamic_frame):
    df = dynamic_frame.toDF()
    df = df.withColumn("skills", explode(split(col("job_skills"), ",")))
    return DynamicFrame.fromDF(df, glueContext, "transformed_skills")

transformed_data = transform_skills(joined_data)

# Save transformed data to S3
glueContext.write_dynamic_frame.from_options(
    frame=transformed_data,
    connection_type="s3",
    connection_options={"path": "s3://linkedin-transformed-data/transformed-data/"},
    format="parquet"
)

job.commit()
