#DemoStr.py

data = "  spam and ham "

result = data.strip()
print(data)
print(result)

result = result.replace("spam", "spam egg")
print(result)
print("-----------")
print(result)
print(result.split())

result2 = ":)".join(result.split())
print(result2)

#regular expression

import re

result = re.search("[0-9]*th", "35th")
print(result.group())

result = re.search("\d{4}", "올해는 2024년 내년은 2025년")
print(result.group())

result = re.search("\d{5}", "우리 동네는 52100")

if result:
    print(result.group())
else:
    print("0")

