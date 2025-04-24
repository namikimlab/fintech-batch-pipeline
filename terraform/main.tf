terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "ap-northeast-2"  # Seoul, Korea 
}

# S3 Bucket for storing data
resource "aws_s3_bucket" "data_bucket" {
  bucket = "fintech-batch-data-${random_id.suffix.hex}"
  force_destroy = true  # for testing ease 

  tags = {
    Name        = "Fintech Batch Data Bucket"
    Environment = "Dev"
  }
}

# Random suffix for unique bucket name
resource "random_id" "suffix" {
  byte_length = 4
}

# Athena Query Results Bucket
resource "aws_s3_bucket" "athena_results" {
  bucket = "fintech-athena-results-${random_id.suffix.hex}"
  force_destroy = true

  tags = {
    Name        = "Athena Query Results Bucket"
    Environment = "Dev"
  }
}

# Athena Workgroup
resource "aws_athena_workgroup" "primary" {
  name = "fintech-batch-workgroup"
  
  configuration {
    result_configuration {
      output_location = "s3://${aws_s3_bucket.athena_results.bucket}/results/"
    }
  }
}
