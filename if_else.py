#score = int(input('Input Score: '))
# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score < 90:
#     grade = "B"
# elif 70 <= score < 80:
#     grade = "C"
# elif 60 <= score < 70:
#     grade = "D"
# else:
#     grade = "F"
    
# print("Grade is " + grade)

d = {"apple":5, "kiwi":10}
for item in d.items():
    print(item)

print("----key value ----")
for k,v in d.items():
    print(k,v)

print(list(range(4,15,3)))

print('-------리스트 임배딩---------')
lst = list(range(1,7))
print([i**2 for i in lst if i % 2 == 0])

d = {100:"apple", 200:"orange", 300:"kiwi"}
print([v.upper() for v in d.values()])

print('----------filtering --------------')
l = [10,25,30]
iterL = filter(None, l)
for i in iterL:
    print("Item:{0}".format(i))

print('----------filtering --------------')
def getBiggerThan20(i):
    return i > 20

iterL = filter(getBiggerThan20, l)
for i in iterL:
    print(f"##Item:{i}")

print('------ filtering lambda-------')    
iterL = filter(lambda x:x>20, l)
for i in iterL:
    print(f"##Item:{i}")