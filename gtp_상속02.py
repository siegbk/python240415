class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}")


class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        super().printInfo()
        print(f"Title: {self.title}")


class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        super().printInfo()
        print(f"Skill: {self.skill}")


# 테스트 코드
def test_classes():
    # Person 클래스 테스트
    p1 = Person(1, "Alice")
    p1.printInfo()
    assert p1.id == 1
    assert p1.name == "Alice"
    
    p2 = Person(2, "Bob")
    p2.printInfo()
    assert p2.id == 2
    assert p2.name == "Bob"

    # Manager 클래스 테스트
    m1 = Manager(3, "Carol", "CTO")
    m1.printInfo()
    assert m1.id == 3
    assert m1.name == "Carol"
    assert m1.title == "CTO"

    m2 = Manager(4, "Dave", "CFO")
    m2.printInfo()
    assert m2.id == 4
    assert m2.name == "Dave"
    assert m2.title == "CFO"

    # Employee 클래스 테스트
    e1 = Employee(5, "Eve", "Python")
    e1.printInfo()
    assert e1.id == 5
    assert e1.name == "Eve"
    assert e1.skill == "Python"

    e2 = Employee(6, "Frank", "Java")
    e2.printInfo()
    assert e2.id == 6
    assert e2.name == "Frank"
    assert e2.skill == "Java"

    # 추가 테스트
    # Manager 클래스
    m3 = Manager(7, "Grace", "CEO")
    m3.printInfo()
    assert m3.id == 7
    assert m3.name == "Grace"
    assert m3.title == "CEO"

    # Employee 클래스
    e3 = Employee(8, "Heidi", "C++")
    e3.printInfo()
    assert e3.id == 8
    assert e3.name == "Heidi"
    assert e3.skill == "C++"

# 테스트 실행
test_classes()
print("모든 테스트가 성공적으로 실행되었습니다.")
