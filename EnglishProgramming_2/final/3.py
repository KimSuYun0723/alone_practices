print("==========3번문제==========")
import re
class fileopen:
    def __init__(self):
        #file = input("파일을 입력하세요: ")
        #self.file = file
        f = open("quaint_vil_sen.txt", "r")
        self.data = f.read()
        f.close()

class word_find(fileopen):
    def word_f(self, fword):
        fword = input("찾고자 하는 단어 입력 : ")
        self.fword = fword
        str0 = f" {fword}" +r"[\.\?\!\s]?"
        p = re.compile(f"{str0}")
        print(p)
        for sen in self.data.split("\n"):
            if p.search(sen):
                print(sen)
a = word_find()
a.word_f("attic")

#3-3
# re.DOTALL / re.S :  메타문자 “.” 은 \n 제외하고 match
# re.IGNORECASE or re.I :  대/소문자 구별없이 match
# 일부 일치 제외
# 문장당 1번
# 결과는 문장 그대로
class n_word_find:
    def word_f(self):
        return
        

            
    
    
    