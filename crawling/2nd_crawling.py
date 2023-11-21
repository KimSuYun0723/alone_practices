from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://ai-dev.tistory.com/2"
html = urlopen(url)
bs_obj = BeautifulSoup(html, "html.parser")

#방법1
print()
table_tag = bs_obj.find_all("table")
table_tag01 = table_tag[0].find_all("td")
for idx, element in enumerate(table_tag01):
    print(idx, element.text)

#방법2
print()
#table01 = bs_obj.find_all("td")
table = bs_obj.find_all("td", {"style":"width: 33.3333%; text-align: center;"})
print(table)
for idx, element in enumerate(table):
    print(idx, element.text)

#목록 정보 추출하기
print()
com_list = bs_obj.find_all("ul")
com_list01 = bs_obj.find_all("ul", {"style":"list-style-type: disc;"})
com_list02 = com_list01[0].find_all("li")
for idx, element in enumerate(com_list02):
    print(idx, element.text)

#/robots.txt