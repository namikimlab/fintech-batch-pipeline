FROM bitnami/spark:latest

# Add Hadoop AWS + AWS SDK JAR (to connect to S3)
ADD https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.6/hadoop-aws-3.3.6.jar /opt/bitnami/spark/jars/
ADD https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.603/aws-java-sdk-bundle-1.12.603.jar /opt/bitnami/spark/jars/
