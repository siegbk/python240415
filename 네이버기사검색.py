import requests
from bs4 import BeautifulSoup

# Naver 검색 URL
url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4'

# requests를 사용하여 URL에서 페이지 내용 가져오기
response = requests.get(url)
response.raise_for_status()  # 에러가 발생하면 예외를 발생시킵니다.

# 페이지 내용을 BeautifulSoup로 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 기사 제목을 추출
# 기사 제목을 포함하는 태그와 클래스를 찾아서 가져옵니다.
# 각 사이트의 HTML 구조에 따라 클래스 이름이나 태그 이름은 달라질 수 있습니다.
# 여기서는 네이버 뉴스의 기사 제목이 "news_tit" 클래스에 들어가 있는 것을 가정합니다.

# 기사 제목을 담을 리스트
titles = []

# 기사 제목을 찾기 위해 적절한 선택자 사용
articles = soup.select('.news_area .news_tit')

# 각 기사 제목 출력
for article in articles:
    # 기사 제목을 추출
    title = article.text
    print(title)
    # 기사 제목을 리스트에 추가
    titles.append(title)
