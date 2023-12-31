from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from bs4 import BeautifulSoup

chromedriver_autoinstaller.install()

options = ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-logging'])
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()), options=options) 

driver.get("https://wis.hufs.ac.kr/src08/jsp/lecture/LECTURE2020L.jsp")

show = driver.find_element(By.NAME, 'btnSearch')
show.click()

page = driver.page_source
bs_obj = BeautifulSoup(page, "html.parser")

win = bs_obj.find_all("txt_navy")
print(win)