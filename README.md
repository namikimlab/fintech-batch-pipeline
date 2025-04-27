# Fintech Batch Data Pipeline

## Overview
This project implements a complete **batch data pipeline** using **Apache Airflow**, **Docker**, **Apache Spark**, **AWS S3**, and **AWS Athena**. The pipeline generates mock credit card transaction data, uploads it to **AWS S3**, processes it using **Apache Spark**, stores the results in **Parquet** format for further analysis, and integrates with **AWS Athena** for querying the processed data.

### Features
- **Data Generation**: Generates mock credit card transaction data using the **Faker** library.
- **S3 Integration**: Uploads generated data to **AWS S3** for storage.
- **Spark ETL**: Processes the transaction data using **Apache Spark** in a Docker container.
- **Airflow Automation**: Orchestrates the entire pipeline using **Apache Airflow**, including task scheduling.
- **Infrastructure as Code (IaC)**: Uses Terraform to provision the necessary cloud resources, such as S3 buckets and Athena. 
- **Athena Integration**: Stores processed data in **Parquet** format on S3 and queries it using **AWS Athena**.



## Project Structure

```plaintext
├── dags/                       # Airflow DAG definitions
│   ├── fintech_batch_dag.py     # Main DAG for orchestrating the pipeline
├── scripts/                     # Python scripts for data generation, uploading, and Spark ETL
│   ├── generate_transactions.py # Generates mock transaction data
│   ├── upload_to_s3.py         # Uploads data to AWS S3
│   ├── spark_etl.py            # Spark ETL job for processing data
├── terraform/                   # Terraform scripts for provisioning cloud resources
│   ├── main.tf                 # Main Terraform configuration file
├── docker-compose.yml           # Docker Compose configuration to run all services
├── Dockerfile.airflow           # Custom Airflow Dockerfile for building containers
└── requirements.txt             # Python dependencies
```

## Tech Stack
- **Apache Airflow**: For orchestrating and scheduling tasks.
- **Docker**: Containerization of services (Airflow, Spark, Postgres).
- **PostgreSQL**: Airflow metadata database.
- **Apache Spark**: ETL processing framework for large-scale data transformation.
- **AWS S3**: Cloud storage for storing and retrieving the data.
- **AWS Athena**: Query engine to run SQL queries on the processed Parquet data stored in S3.
- **Faker**: Python library for generating fake data.
- **boto3**: AWS SDK for interacting with S3.
- **Terraform**: Infrastructure as code for provisioning AWS resources like S3 buckets and IAM roles.

## Setup Instructions
### Prerequisites
- Docker and Docker Compose installed on your machine.
- Terraform installed on your machine.
- AWS Account with access to S3 and Athena.

### Installation Steps
1. Clone the repository:
```
git clone https://github.com/namikimlab/fintech-batch-pipeline.git
cd fintech-batch-pipeline
```

2. Set up AWS resources using Terraform:
- Install Terraform if you don't have it.
- Initialize and apply Terraform:
```
cd terraform
terraform init
terraform apply
```

3. Build and start the Docker containers: This command will build the images and start the necessary containers for Airflow, Spark, and Postgres.
```
docker compose up --build -d
```

4. Access Airflow UI:

- Open your browser and navigate to http://localhost:8080.
- Log in using the default credentials:
    - Username: admin
    - Password: admin
- Set `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` as Airflow Variables in the Airflow UI.

5. Trigger the DAG:
- Once logged into the Airflow UI, locate the `fintech_batch_pipeline` DAG and trigger it manually.


## Usage
- The DAG will perform the following steps:

1. Generate Data: Using the generate_transactions.py script, mock credit card transaction data is generated and saved as a CSV.

2. Upload to S3: The data is uploaded to AWS S3 using the upload_to_s3.py script.

3. Spark ETL: The spark_etl.py script processes the data using Apache Spark in a Docker container.

- Monitor each task's progress in the Airflow UI.

- Check the logs for any errors or status updates for each task in the Airflow UI.

4. Transformed data is stored in Parquet format on S3, optimized for querying with AWS Athena.


## Troubleshooting
* Missing Files: Ensure that all paths to scripts and volumes are correctly mapped in `docker-compose.yml`.


## Future Improvements
### Monitoring & Logging
- Enhance Airflow logging for better traceability.
- Add error handling, retries, and alerts (e.g., Slack or Email notifications).
### Performance Optimization
- Optimize Spark jobs (e.g., partitioning, tuning parallelism).
- Improve query performance with partitioned and clustered tables.
### Data Validation & Quality
- Integrate data quality checks (e.g., Great Expectations).
- Validate data consistency and integrity across the pipeline.
### Scaling & Robustness
- Scale Spark workers as data volume grows.
- Consider incorporating Kubernetes for bigger job. 
### Data Analysis & Visualization
- Build dashboards with Looker, Google Data Studio, or Power BI.
- Incorporate machine learning models for fraud detection or anomaly analysis.
### CI/CD Automation
- Use GitHub Actions or Jenkins to automate DAG deployments and Terraform changes.
### Documentation & Testing
- Add end-to-end tests for pipeline integrity.
- Improve code documentation and maintainability.