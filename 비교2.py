# 리스트와 튜플 비교

# 리스트와 튜플 선언
list1 = [1, 2, 3, 4, 5]
tuple1 = (1, 2, 3, 4, 5)

# 자료형 확인
print(type(list1))  # <class 'list'>
print(type(tuple1))  # <class 'tuple'>

# 요소 변경
try:
  list1[0] = 10
  print(list1)  # [10, 2, 3, 4, 5]
except TypeError as e:
  print(e)  # 'list' objects are mutable

try:
  tuple1[0] = 10
except TypeError as e:
  print(e)  # 'tuple' objects are immutable


# 요소 추가
list1.append(6)
print(list1)  # [10, 2, 3, 4, 5, 6]

try:
  tuple1.append(6)
except AttributeError as e:
  print(e)  # 'tuple' object has no attribute 'append'


# 슬라이싱
list_slice = list1[1:3]
print(list_slice)  # [2, 3]

tuple_slice = tuple1[1:3]
print(tuple_slice)  # (2, 3)


# 반복
for i in list1:
  print(i)

for i in tuple1:
  print(i)


# 길이 확인
print(len(list1))  # 6
print(len(tuple1))  # 5


# 메모리 확인
import sys

print(sys.getsizeof(list1))  # 48
print(sys.getsizeof(tuple1))  # 40

