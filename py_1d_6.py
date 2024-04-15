x=5

def set(val):
    global x
    x=val

def add(val):
    global x
    x+=val

print(x)

set(6)

print(x)

add(10)
print(x)