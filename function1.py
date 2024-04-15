#function1.py

#1 함수 정의
def setValue(newValue):
    x = newValue
    print('local val:', x)


#2 호출
retValue = setValue(5)
print(retValue)

#return tuple
def swap(x,y):
    return y,x

print(swap(3,4))


x = 5
def func1(a):
    return a+x

print(func1(1))

def func2(a):
    x = 10
    return a+x

print(func2(1))


#debugging
#교집합 리턴 함수
def intersect(prelist, postlist):
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

print(intersect("HAM", "SPAM"))

def intersect2(prelist, postlist):
    # 두 문자열을 집합으로 변환하여 교집합을 구함
    result_set = set(prelist) & set(postlist)
    # 교집합을 리스트로 변환하여 반환
    return list(result_set)

print(intersect2("HAM", "SPAM"))


def times2(a=10, b=20):
    return a*(b+1)

print(times2())
print(times2(5))
print(times2(5,6))
print(times2(b=5,a=3))

def connectURI(server, port):
    strURL = "https://"+server+":"+port
    return strURL

print(connectURI("multi.com", "80"))
print(connectURI( port ="80", server = "multi.com"))


