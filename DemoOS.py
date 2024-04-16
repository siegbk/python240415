#DemoOS.py

import random

print(random.random())
print(random.random())
print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])
print(random.sample(range(20), 10))
print(random.sample(range(20), 10))

list =random.sample(range(1, 46), 6)
list.sort()
print(list)


from os.path import *
print(abspath("python.exe"))
print(basename("c:\\work\\python.exe"))
print(getsize("c:\\python310\\python.exe")/1024)

if exists("c:\\python310\\python.exe"):
    print("0")
else:
    print("x")

from os import *
print("os name :", name)
print("environment:", environ)

#system("notepad.exe")

import glob

result = glob.glob("c:\\work\\*.py")
print('------------------')
print(result)