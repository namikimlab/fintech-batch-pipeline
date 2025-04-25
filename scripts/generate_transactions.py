from faker import Faker
import pandas as pd
import random
import uuid

fake = Faker('ko_KR')

categories = ['식음료', '교통', '쇼핑', '여행', '의료', '엔터테인먼트', '교육', '통신', '보험', '금융서비스']
regions = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']

def generate_transaction():
    return {
        'transaction_id': str(uuid.uuid4()),
        'transaction_time': fake.date_time_between(start_date='-3M', end_date='now'),
        'card_number': '****-****-****-' + str(random.randint(1000,9999)),
        'customer_id': str(uuid.uuid4()),
        'merchant_id': str(uuid.uuid4()),
        'merchant_name': fake.company(),
        'merchant_region': random.choice(regions),
        'amount': round(random.uniform(1000, 1000000), 2),
        'category': random.choice(categories)
    }

n = 10000  # number of transactions for testing 
data = [generate_transaction() for _ in range(n)]

df = pd.DataFrame(data)
df.to_csv('card_transactions.csv', index=False, encoding='utf-8-sig')

print(f"{n}건의 거래 데이터를 생성했습니다")
