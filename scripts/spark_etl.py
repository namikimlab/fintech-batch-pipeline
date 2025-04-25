from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum

# Create Spark session (with connection to S3)
spark = SparkSession.builder \
    .appName("Fintech ETL") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.fs.s3a.aws.credentials.provider", 
            "com.amazonaws.auth.EnvironmentVariableCredentialsProvider") \
    .getOrCreate()

# S3 path 
raw_s3_path = "s3a://fintech-batch-data-6d065094/raw/card_transactions.csv"
processed_s3_path = "s3a://fintech-batch-data-6d065094/processed/"

# Read data (CSV)
df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(raw_s3_path)

# Transform (Transaction amount per region)
agg_df = df.groupBy("merchant_region") \
    .agg(_sum(col("amount")).alias("total_amount"))

# Save to Parquet (S3 processed/)
agg_df.write.mode("overwrite").parquet(processed_s3_path)

print("ETL 완료: Parquet 저장 완료!")
