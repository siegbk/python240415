# Person.py 
class Person:
    def __init__(self):
        self.__name = "default name"
    def print(self):
        print(f"My name is {self.__name}")
    def __str__(self):
        return f"name .....{self.__name}"

p1 = Person()
p2 = Person()
p1.__name = "전우치"
p1.print()
p2.print()
#print(p1.name)
print(p1)

