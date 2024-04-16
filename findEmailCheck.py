import re

def is_valid_email(email):
    # 이메일 주소 확인을 위한 정규 표현식
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    # 정규 표현식에 email이 일치하는지 확인
    if re.match(email_pattern, email):
        return True
    else:
        return False

# 테스트 이메일 주소
test_emails = [
    "test@example.com",
    "user.name@domain.co.uk",
    "user+test@domain.com",
    "invalid@domain,com",
    "invalid@domain",
    "invalid@domain.com-",
    "@invalid.com",
]

# 각 이메일 주소를 확인하여 유효한지 검사
for email in test_emails:
    if is_valid_email(email):
        print(f"{email}는 유효한 이메일 주소입니다.")
    else:
        print(f"{email}는 유효하지 않은 이메일 주소입니다.")
