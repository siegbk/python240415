#web2.py
import requests
from bs4 import BeautifulSoup


url = "https://www.daangn.com/fleamarket/"
#페이지 실행 요청
response = requests.get(url)

#검색이 용이한 객체
soup = BeautifulSoup(response.text, "html.parser")

f = open("daangn.txt", "a+", encoding="utf-8")
posts = soup.find_all("div", attrs={"class":"card-desc"})
for post in posts:
    titleElem = post.find("h2", attrs={"class":"card-title"})
    title = titleElem.text.strip()
    priceElem = post.find("div", attrs={"class":"card-price"})
    price = priceElem.text.strip()
    regionElem = post.find("div", attrs={"class":"card-region-name"})
    region = regionElem.text.strip()
    #print(f"{title}, {price}, {region}")
    f.write(f"{title}, {price}, {region}\n")

#file close
f.close()    

# <div class="card-desc">
# <h2 class="card-title">아이폰 15</h2>
# <div class="card-price ">
# 100,000원
# </div>
# <div class="card-region-name">
# 서울 노원구 중계동
# </div>

