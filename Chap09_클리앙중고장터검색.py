#Chap09_클리앙중고장터검색.py
# coding:utf-8
from bs4 import BeautifulSoup #정적인 사이트에 강하다.
#python built lib
import urllib.request
#regular expression
import re 

f = open("cl.txt", "wt", encoding="utf-8")
for n in range(0,3):
        #클리앙의 중고장터 주소 
        url ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
        print(url)
        data = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(data, 'html.parser')
        list = soup.find_all('span', attrs={'data-role':'list-title-text'})
        # <span class="subject_fixed" data-role="list-title-text" title="맥북프로 M2 13인치 24/512 실버">
		# 		맥북프로 M2 13인치 24/512 실버
		# </span>
        for item in list:
            title = item.text.strip()
            #print(title)
            #키워드 검색
            if re.search("아이폰", title):
                  print(title)
                  f.write(f"{title}\n")

f.close()


#https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=1