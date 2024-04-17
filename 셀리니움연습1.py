#selenium 연습1.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#크롬 드라이버 실행
driver = webdriver.Chrome()

#url address
driver.get("https://www.google.co.kr")

#3sec wait
time.sleep(3)

#<textarea class="gLFyf" 
#aria-controls="Alh6id" aria-owns="Alh6id" autofocus="" title="검색" value="" jsaction="paste:puy29d;" aria-label="검색" aria-autocomplete="both" aria-expanded="true" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" 
# id="APjFqb" maxlength="2048" name="q" role="combobox" rows="1" spellcheck="false" data-ved="0ahUKEwjVtt-ZzciFAxUXgVYBHem0A5IQ39UDCAY" aria-activedescendant="" style=""></textarea>

#searchBox = driver.find_element(By.CLASS_NAME, "gLFyf")
searchBox = driver.find_element(By.XPATH, "//*[@id='APjFqb']")
# // 전체 계층 모든 요소
# @ 검색, @id =id 검색

searchBox.send_keys("맥북")
searchBox.send_keys(Keys.ENTER)

time.sleep(10)

