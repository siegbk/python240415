import requests
from bs4 import BeautifulSoup

def crawl_naver_blog(search_keyword):
    # Naver 블로그 검색 결과 페이지 URL (검색어 포함)
    url = f'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}'

    # URL에서 페이지 내용 가져오기
    response = requests.get(url)
    response.raise_for_status()  # 요청이 성공적으로 처리되었는지 확인
    
    # 페이지 내용을 BeautifulSoup로 파싱
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 결과를 담을 리스트
    results = []

    # 블로그 검색 결과에서 각 항목을 추출
    for item in soup.find_all('li', class_='bx'):
        # 블로그명
        blog_name = item.find('a', class_='api_txt_lines').text
        
        # 블로그 주소
        blog_url = item.find('a', class_='api_txt_lines')['href']
        
        # 제목
        title = item.find('a', class_='api_txt_lines').text
        
        # 포스팅 날짜
        date_element = item.find('span', class_='sub_time')
        post_date = date_element.text if date_element else 'Unknown'
        
        # 결과를 딕셔너리로 저장
        results.append({
            'blog_name': blog_name,
            'blog_url': blog_url,
            'title': title,
            'post_date': post_date
        })

    return results

# 예시: "반도체" 키워드로 크롤링
search_keyword = "아이폰15"
results = crawl_naver_blog(search_keyword)

# 결과 출력
for idx, result in enumerate(results, start=1):
    print(f"Result {idx}:")
    print(f"블로그명: {result['blog_name']}")
    print(f"블로그 주소: {result['blog_url']}")
    print(f"제목: {result['title']}")
    print(f"포스팅 날짜: {result['post_date']}")
    print()  # 줄 바꿈
