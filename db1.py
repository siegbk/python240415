#db1.py
import sqlite3

con =sqlite3.connect(":memory:")

cur = con.cursor()

table = "PhoneBook"

cur.execute(f"Create table {table} (Name text, PhoneNum text);")
cur.execute(f"Insert into {table} values ('홍길동', '010-222');")

name = "전우치"
phoneNum = "010-333"
cur.execute(f"Insert into {table} values (?,?);", (name, phoneNum))

#다중행 입력
datalist = (("Hong", "010-123"), ('Brad', '010-567'), ("Kim", '010-1111'))
cur.executemany(f"Insert into {table} values (?,?);", datalist)

cur.execute(f"Select * From {table} Order by 1;")
# for row in cur:
#     print(row)

print('cur.fetchone()')
print(cur.fetchone())
print('cur.fetchmany(2)')
print(cur.fetchmany(2))


cur.execute(f"Select * From {table} Order by 1 desc;")
print('cur.fetchall()')
print(cur.fetchall())

