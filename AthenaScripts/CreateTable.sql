CREATE EXTERNAL TABLE IF NOT EXISTS linkedin_transformed_data (
  job_link STRING,
  last_processed_time TIMESTAMP,
  got_summary STRING,
  got_ner STRING,
  is_being_worked STRING,
  job_title STRING,
  company STRING,
  job_location STRING,
  first_seen TIMESTAMP,
  search_city STRING,
  search_country STRING,
  search_position STRING,
  job_level STRING,
  job_type STRING,
  skills STRING
)
PARTITIONED BY (job_type STRING, search_country STRING)
STORED AS PARQUET
LOCATION 's3://linkedin-transformed-data/transformed-data/';
