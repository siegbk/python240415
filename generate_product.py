from openpyxl import Workbook
import random
import string

# 파일 경로
file_path = "c:\\work\\products.xlsx"

# Workbook 생성
wb = Workbook()
ws = wb.active

# 시트 제목 설정
ws.title = "Products"

# 헤더 행 설정
headers = ["제품ID", "제품명", "수량", "가격"]
ws.append(headers)

# 제품 데이터 생성
def generate_product_data():
    product_id = random.randint(1000, 9999)  # 제품 ID를 1000에서 9999 사이의 랜덤한 정수로 생성
    product_name = ''.join(random.choices(string.ascii_uppercase, k=5))  # 제품명을 대문자 5글자로 생성
    quantity = random.randint(1, 100)  # 수량을 1에서 100 사이의 랜덤한 정수로 생성
    price = random.randint(10, 1000)  # 가격을 10에서 1000 사이의 랜덤한 정수로 생성
    return product_id, product_name, quantity, price

# 100개의 제품 데이터 생성 및 시트에 추가
for _ in range(100):
    product_data = generate_product_data()
    ws.append(product_data)

# 파일 저장
wb.save(file_path)

print(f"Data saved to {file_path}")
