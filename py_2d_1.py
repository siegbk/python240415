#ifelse.py

for i in range(10):
    score = int(input("in :"))
    if score == 0:
        break

    if 90 <= score <= 100:
        grade = 'A'
    else:
        grade = 'F'
    print(grade)

