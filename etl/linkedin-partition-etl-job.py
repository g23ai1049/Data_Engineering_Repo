import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.sql.functions import year, month, dayofmonth

# Initialize Glue context
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Read the data from S3
input_data = "s3://linkedin-transformed-data/"
df = spark.read.json(input_data)

# Extract year, month, and day from first_seen timestamp
df = df.withColumn("year", year(df.first_seen)) \
       .withColumn("month", month(df.first_seen)) \
       .withColumn("day", dayofmonth(df.first_seen))

# Write the data to S3 in a partitioned format
output_data = "s3://linkedin-partitioned-data/"
df.write.partitionBy("year", "month", "day").parquet(output_data)

# Commit the job
job.commit()
