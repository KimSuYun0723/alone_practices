from bs4 import BeautifulSoup
html_doc = """
<!doctype html>
<html>
    <head>
        <title>
            기초 웹 크롤링
        </title>
    </head>
    <body>
        크롤링을 해봅시다.
    </body>
</html>
"""

bs_obj = BeautifulSoup(html_doc, "html.parser")
head = bs_obj.find("head")
body = bs_obj.find("body")
#div_total = bs_obj.find_all("div") --> 만난 div를 모두 list에 저장
#div2 = div_total[1] --> 인덱스로 조절 가능
#print(div2.text) --> 테그 내의 텍스트만 추출

print(head)
print(body)