# list, tuple, set, dict 데이터 형식의 메서드 비교

# 1. list
my_list = [1, 2, 3, 4, 5]

# list의 주요 메서드
my_list.append(6)  # 요소 추가
my_list.remove(3)  # 특정 요소 제거
my_list.sort()  # 정렬
print("List:", my_list)

# 2. tuple
my_tuple = (1, 2, 3, 4, 5)

# tuple은 불변(immutable)이므로 요소 추가, 제거, 변경이 불가능합니다.
# 주로 요소 조회 및 인덱싱에 사용됩니다.
print("Tuple:", my_tuple)
print("Tuple 요소 수:", len(my_tuple))

# 3. set
my_set = {1, 2, 3, 4, 5}

# set의 주요 메서드
my_set.add(6)  # 요소 추가
my_set.remove(2)  # 특정 요소 제거
my_set.update({7, 8})  # 여러 요소 추가
print("Set:", my_set)

# 4. dict
my_dict = {'a': 1, 'b': 2, 'c': 3}

# dict의 주요 메서드
my_dict['d'] = 4  # 새로운 키-값 쌍 추가
my_dict.pop('b')  # 특정 키-값 쌍 제거
print("Dict:", my_dict)

# dict의 키-값 쌍을 반복적으로 순회
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

# dict의 키, 값, 키-값 쌍에 접근
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items:", my_dict.items())


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

