#db1.py
import sqlite3

# con =sqlite3.connect(":memory:")
#file 
con =sqlite3.connect("c:\\work\\sample2.db")
cur = con.cursor()

#table = "PhoneBook"
table = "Employee"

#cur.execute(f"Create table if not exists {table} (Name text, PhoneNum text);")
#cur.execute(f"Insert into {table} values ('홍길동', '010-222');")

#name = "전우치"
#phoneNum = "010-333"
#cur.execute(f"Insert into {table} values (?,?);", (name, phoneNum))

#다중행 입력
#datalist = (("Hong", "010-123"), ('Brad', '010-567'), ("Kim", '010-1111'))
#cur.executemany(f"Insert into {table} values (?,?);", datalist)


cur.execute(f"Select * From {table} Order by 1;")
# for row in cur:
#     print(row)

print(cur.fetchall())

#con.commit()