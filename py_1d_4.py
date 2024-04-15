print('h')

strA = "Python is vert powerful Lang"
strB = "한글한글파이썬이즈심플"

print(len(strA))
print(len(strB))

print(strA[0])
print(strA[0:6])
print(strA[6])
print(strA[-1])
print(strA[-4:])
print(strA[-5:])

print('--------------list')
list = [10,200,31,4]
list.reverse()

print(list)

list.sort()
list.reverse()
print(list)

list.append(5)
list.append(6006)

color = ["red", "blue"]

color.append("green")
color.insert(1, "pink")
color.remove("red")

print(color)
color.sort()
print(color)

a = {1,2,3,4,7}
b = {1,7,-1}
print(a)

print(b)

print(a.union(b))




print('----Set----')

a= {1,2,3,3}
b = {3,4,4,5}

print(a)
print(b)


print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

tp = (10,20,30)

print(tp)


def calc(a,b):
    return a+b,a*b

result = calc(3,4)
print(result)
print("id %d, name: %d" % (result[0], result[1]))


tp2 = (5,6)
result = calc(*tp2)
print(result)

print(calc(*result))

