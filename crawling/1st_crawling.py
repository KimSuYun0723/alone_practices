from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://ai-dev.tistory.com/1"
html = urlopen(url)
bs_obj = BeautifulSoup(html, "html.parser")

#제목 추출
title = bs_obj.find_all("h1")
print(title[1].text)

#본문 내용 추출
contents = bs_obj.find_all("p")
print(contents[1].text)