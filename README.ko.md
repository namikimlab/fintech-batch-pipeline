[🇺🇸 English](./README.md) | [🇰🇷 한국어](./README.ko.md)

# 핀테크 배치 데이터 파이프라인

## 개요  
이 프로젝트는 Apache Airflow, Docker, Apache Spark, AWS S3, AWS Athena를 활용해 핀테크 배치 데이터 파이프라인을 구축한 것입니다.
가상의 신용카드 거래 데이터를 생성해 AWS S3에 업로드하고, Apache Spark로 데이터를 정제 및 가공한 뒤, Parquet 형식으로 저장합니다. 이후 AWS Athena를 통해 데이터를 쉽게 쿼리하고 분석할 수 있도록 구성했습니다.



## 주요 기능
- **데이터 생성**: **Faker** 라이브러리를 이용해 가상의 신용카드 거래 데이터를 생성합니다.  
- **S3 연동**: 생성된 데이터를 **AWS S3**에 업로드하여 저장합니다.  
- **Spark ETL**: Docker 컨테이너 내에서 **Apache Spark**를 사용해 데이터를 가공합니다.  
- **Airflow 자동화**: 전체 파이프라인을 **Apache Airflow**로 자동화하며, 작업 스케줄링도 포함합니다.  
- **IaC(Infrastructure as Code)**: Terraform으로 S3 버킷, Athena 등 필요한 클라우드 리소스를 자동으로 생성합니다.  
- **Athena 통합**: S3에 저장된 **Parquet** 데이터를 **AWS Athena**로 쿼리할 수 있습니다.


## 프로젝트 구조

```plaintext
├── dags/                       # Airflow DAG 정의
│   ├── fintech_batch_dag.py     # 파이프라인을 오케스트레이션하는 메인 DAG
├── scripts/                     # 데이터 생성, 업로드, Spark ETL 관련 파이썬 스크립트
│   ├── generate_transactions.py # 거래 데이터 생성
│   ├── upload_to_s3.py         # S3로 데이터 업로드
│   ├── spark_etl.py            # Spark ETL 처리 스크립트
├── terraform/                   # 클라우드 인프라 생성용 Terraform 스크립트
│   ├── main.tf                 # 메인 Terraform 설정 파일
├── docker-compose.yml           # 모든 서비스를 실행하는 Docker Compose 설정
├── Dockerfile.airflow           # Airflow 컨테이너를 위한 커스텀 Dockerfile
└── requirements.txt             # 필요한 파이썬 패키지 목록
```

## 기술 스택

- **Apache Airflow**: 파이프라인의 태스크를 오케스트레이션하고 스케줄링합니다.
- **Docker**: Airflow, Spark, PostgreSQL 등을 컨테이너로 실행하여 환경 구성을 일관되게 유지합니다.
- **PostgreSQL**: Airflow의 메타데이터를 저장하는 데이터베이스로 사용됩니다.
- **Apache Spark**: 대규모 데이터를 효율적으로 처리하기 위한 ETL 프레임워크입니다.
- **AWS S3**: 생성된 데이터와 처리된 데이터를 저장하는 클라우드 스토리지입니다.
- **AWS Athena**: S3에 저장된 Parquet 파일을 SQL로 쿼리할 수 있는 분석 도구입니다.
- **Faker**: 신용카드 거래 데이터를 시뮬레이션하기 위한 가상 데이터 생성 라이브러리입니다.
- **boto3**: AWS S3와 상호작용하기 위한 Python SDK입니다.
- **Terraform**: S3 버킷, IAM 역할, Athena 테이블 등 AWS 인프라를 코드로 관리합니다.


## 설치 및 실행

### 사전 조건

- Docker 및 Docker Compose 설치
- Terraform 설치
- AWS 계정 (S3 및 Athena 사용 권한 포함)


### 설치 과정
1. 리포지토리 복사:
```bash
git clone https://github.com/namikimlab/fintech-batch-pipeline.git
cd fintech-batch-pipeline
```

2. Terraform으로 AWS 리소스를 생성:
```bash
cd terraform
terraform init
terraform apply
```

3. Docker 컨테이너를 빌드 및 실행:
```bash
docker compose up --build -d
```

4. Airflow UI에 접속:

- 브라우저에서 http://localhost:8080 접속
- 로그인 정보:
    - Username: admin
    - Password: admin
- Airflow UI Admin > Variables 에 다음 AWS 키들을 추가: 
    - `AWS_ACCESS_KEY_ID`
    - `AWS_SECRET_ACCESS_KEY` 

5. DAG 실행:
- Airflow UI에서 fintech_batch_pipeline DAG를 수동으로 트리거합니다.


## 사용 방법
DAG를 통해 아래 과정을 자동화 할 수 있습니다.

1. **데이터 생성**  
   `generate_transactions.py` 스크립트를 사용하여 가상의 신용카드 거래 데이터를 생성하고, 이를 CSV 형식으로 저장합니다.

2. **S3 업로드**  
   `upload_to_s3.py` 스크립트를 이용하여 생성된 데이터를 AWS S3에 업로드합니다.

3. **Spark ETL 처리**  
   `spark_etl.py` 스크립트가 Docker 컨테이너 내에서 Apache Spark를 사용해 데이터를 처리합니다.

- 각 태스크의 진행 상황은 Airflow UI에서 모니터링할 수 있습니다.
- 에러 로그 및 상태 업데이트는 Airflow UI의 각 태스크 로그를 통해 확인할 수 있습니다.

4. **결과 저장**  
   처리된 데이터는 Parquet 포맷으로 S3에 저장되며, AWS Athena에서 쿼리할 수 있습니다.

## 문제 해결

- **Missing Files: 파일 누락**  
  `docker-compose.yml` 파일 내에 스크립트 경로 및 볼륨 마운트가 올바르게 설정되었는지 확인하세요.



## 향후 개선 사항 (Future Improvements)

### 📈 모니터링 및 로깅
- Airflow 로그 수준 향상을 통해 추적 가능성 향상
- 에러 핸들링, 재시도 로직, 알림(Slack, 이메일 등)을 추가

### 🚀 성능 최적화
- Spark 작업을 파티셔닝 및 병렬 처리 튜닝 등을 통해 최적화
- 파티셔닝 및 클러스터링 테이블을 활용하여 Athena 쿼리 성능을 개선

### ✅ 데이터 검증 및 품질
- **Great Expectations**와 같은 도구를 활용하여 데이터 품질 검사를 추가
- 파이프라인 전반의 데이터 정합성과 일관성을 검증

### 📊 데이터 분석 및 시각화
- **Looker**, **Google Data Studio**, **Power BI** 등을 활용하여 대시보드를 구축
- 이상 감지나 사기 탐지를 위한 머신러닝 모델을 접목 

### 🔁 CI/CD 자동화
- GitHub Actions 또는 Jenkins를 사용하여 DAG 배포 및 Terraform 변경을 자동화


---
Made with 🧡 by Nami Kim
[Blog](https://namixkim.com) | [GitHub](https://github.com/namikimlab) | [LinkedIn](https://linkedin.com/in/namixkim)