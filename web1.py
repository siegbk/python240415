#web1.py
from bs4 import BeautifulSoup

#loading file
page = open("c:\\work\\Chap09_test.html", "rt", encoding="utf-8").read()

#Object for search
soup = BeautifulSoup(page, "html.parser")

#show all
#print(soup.prettify())

#<p> tag search all
#print(soup.find_all("p"))

#<p> tag search  each
#print(soup.find("p"))

#<p> tag and class='outer-text search
#print(soup.find_all("p", class_ = "outer-text"))

#조건: attrs 속성명
#print(soup.find_all("p", attrs={"class":"outer-text"}))

#id속성 검색
#print(soup.find_all(id="first"))

#태그 내부에 문자열: .text, get_text()
for tag in soup.find_all("p"):
    #내부 문자열 리턴
    title = tag.text.strip()
    #줄바꿈 문자 변화
    title = title.replace("\n", "")
    print(title)
