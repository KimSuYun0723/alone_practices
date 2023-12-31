"""from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.livesport.com/kr/team/manchester-united/ppjDR086/"
html = urlopen(url)
bs_obj01 = BeautifulSoup(html, "html.parser")
win01 = bs_obj01.find_all("span", {"class": "wld wld--w"}) #[]
# bs4로는 한계임. 동적 웹페이지에서 비어있는 것으로 뜸. 페이지 소스에서도 안뜸
"""
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome() #C:/Users/jenny/Downloads/chromedriver.exe _ 현재 셀레늄은 크롬드라이브 다운 안해도 사용 가능

driver.implicitly_wait(3)
driver.get("https://www.livesport.com/kr/team/manchester-united/ppjDR086/")

page = driver.page_source
bs_obj = BeautifulSoup(page, "html.parser")

win = bs_obj.find_all("div", {"class": "formIcon formIcon--w"}) #tag, class
print(win)
