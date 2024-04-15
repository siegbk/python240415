

a = set((1,2,3))
b = list(a)
b.append(4)
print(b)
print(type(b))


dictA = {1:"a1", 3:"c31", 4:"d4000"}

print(dictA)

dictA[5]="e5"

print(dictA)

for item in dictA.items():
    print(item)
    print(type(item))

del dictA[3]    

for item in dictA.items():
    print(item)


print(len(dictA))

dictA[1010] = "th"
print(len(dictA))


for item in dictA.items():
    print(item, end=' ')
print()

