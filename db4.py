import sqlite3

class ElectronicsDatabase:
    def __init__(self, db_name):
        # 데이터베이스에 연결
        self.conn = sqlite3.connect(db_name)
        self.create_table()
    
    def create_table(self):
        # 제품 테이블을 생성
        create_table_query = """
        CREATE TABLE IF NOT EXISTS electronics (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            price REAL NOT NULL
        );
        """
        self.conn.execute(create_table_query)
        self.conn.commit()
    
    def insert_product(self, product_name, price):
        # 제품을 추가
        insert_query = """
        INSERT INTO electronics (product_name, price)
        VALUES (?, ?);
        """
        self.conn.execute(insert_query, (product_name, price))
        self.conn.commit()
    
    def update_product(self, product_id, product_name=None, price=None):
        # 제품을 업데이트
        update_query = "UPDATE electronics SET"
        params = []
        
        if product_name:
            update_query += " product_name = ?,"
            params.append(product_name)
        
        if price is not None:
            update_query += " price = ?,"
            params.append(price)
        
        # 마지막 콤마 제거
        update_query = update_query.rstrip(',')
        update_query += " WHERE product_id = ?"
        params.append(product_id)
        
        self.conn.execute(update_query, params)
        self.conn.commit()
    
    def delete_product(self, product_id):
        # 제품을 삭제
        delete_query = "DELETE FROM electronics WHERE product_id = ?"
        self.conn.execute(delete_query, (product_id,))
        self.conn.commit()
    
    def select_product(self, product_id):
        # 특정 제품을 선택
        select_query = "SELECT * FROM electronics WHERE product_id = ?"
        cursor = self.conn.execute(select_query, (product_id,))
        product = cursor.fetchone()
        return product
    
    def select_all_products(self):
        # 모든 제품을 선택
        select_query = "SELECT * FROM electronics"
        cursor = self.conn.execute(select_query)
        products = cursor.fetchall()
        return products

# 전자제품 데이터베이스를 사용하기 위해 초기화
#db_name = 'electronics.db'
db_name = "c:\\work\\electronics.db"
db = ElectronicsDatabase(db_name)

# 샘플 데이터 10개 추가
sample_data = [
    ("노트북", 1000000),
    ("스마트폰", 800000),
    ("태블릿", 500000),
    ("모니터", 300000),
    ("헤드폰", 100000),
    ("스피커", 150000),
    ("키보드", 50000),
    ("마우스", 30000),
    ("카메라", 700000),
    ("프린터", 250000)
]

# 샘플 데이터 추가
for product_name, price in sample_data:
    db.insert_product(product_name, price)

# 모든 제품 출력
print("모든 제품:")
products = db.select_all_products()
for product in products:
    print(product)
