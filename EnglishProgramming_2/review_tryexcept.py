#4p &11p
class Fourcal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def div(self):
        result = self.first / self.second
        return result
try:
    a = Fourcal("a", 0)
    print(a.div())
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다!")
except TypeError:
    print("숫자를 입력하세요!")

#5p
class File:
    def __init__(self,file):
        f = open(file, "r")
        self.data = f.read()
        f.close()

try:
    a = File()
    a()
except TypeError:
    print("File이 없어요")


class letter_counter:
    def __init__(self, word):
        self.word = word
    def counter(self):
        num_letter = len(self.word)
        print ("The length of the word {0} is {1}".format(self.word, num_letter))

try:
    b = letter_counter("apple", "pear")
    b.counter()
except TypeError as error: 
    print(error)
    print("문자를 입력하세요! ({0})".format(error))
#len에 int들어가는 것 & argument 개수도 전부 Typeerror
#--> 그래서 구분 필요함_
except TypeError as error:
    print("한 단어만 입력하세요! ({0})".format(error))
    #어떻게 해.........ㅜㅜㅜㅜㅜ
    
#16p- try~except~else(except 안만나면 실행하는 블록)

#18p- try~except~finally(예외 발생이랑 상관없이 실행)
    #try->else->finally
    #try->except->finally

#오류 회피 --> pass쓰면 됨

#거의 모든 예외형식들은 Exception 클래스로부터 파생됨.

# 24p
class letter_counter:
    def __init__(self, word):
        if int(word):
            raise Exception("단어를 입력하세요!") #오류메시지
        else:
            self.word = word
    def counter(self):
        num_letter = len(self.word)
        print ("The length of the word {0} is {1}".format(self.word, num_letter))
try:
    b = letter_counter("apple")
    b.counter()
except TypeError as error:
    print("한 단어만 입력하세요! ({0})".format(error))
except Exception as error: # error, err, e
    print("예외! ({0})".format(error))

#26p
class letter_counter:
    def __init__(self, word):
        if len(word.split(" "))>1:
            raise Exception("2 words!!!")
        elif int(word): 
            raise Exception("문자로된 숫자 입력!")
        else:
            self.word = word            
    def counter(self):
        num_letter = len(self.word)
        print ("The length of the word {0} is {1}".format(self.word, num_letter))

try:
    b = letter_counter("124")
    b.counter()
except TypeError as error:
    print("단어 2개 넣음 : ({0})".format(error))
except AttributeError as error:
    print("숫자 넣음 : ({0})".format(error))
except Exception as error: 
    print("예외 : ({0})".format(error))

#27p- 사용자 정의 예외
class myerror_(Exception):
    def __str__(self): #str 반환
        #사용자 정의 예외의 예외 메시지가 되는 것
        return "글자를 입력하세요" 
        
class letter_counter:
    def __init__(self, word):
        if int(word):
            raise myerror_()
        else:
            self.word = word
    def counter(self):
        num_letter = len(self.word)
        print ("The length of the word {0} is {1}".format(self.word, num_letter))

try:
    c = letter_counter("123")
    c.counter()
except myerror_ as error:
    print("예외가 발생했습니다. {0}".format(error))
        
#29p - 실습
""" 아래 예외를 모두 포함하여 예외처리 해보기
• 숫자를 입력한 경우
• 단어를 2개 (argument 2개) 입력한 경우
• 단어를 띄어쓰기 포함 2개 입력한 경우"""

#30p-실습
"""사용자 정의 예외 처리 실습 1
• 사전(데이터)에 없는 단어를 검색했을 때 오류 발생시키고 예외처리
dic = {"abnormal": "adjective", 
"adhere": "verb", 
"ant": "noun", 
"apple": "noun"}"""

#31p-실습 (과제였음)
"""사용자 정의 예외 처리 실습 2
• 사이트에 가입할 때 별명을 입력할 때가 있다. 이미 존재하는 별명이거나, 사이
트에서 허용하지 않는 문자열이 포함되어 있는 경우에 예외 처리를 하고 다시
입력하도록 하는 프로그램을 작성해보자
• 이미 존재하는 별명 예시
• exist_nick = [“강아지”, “토끼”, “병아리”, “다람쥐”]
• 허용하지 않는 문자열 예시
• disallow = [“바보”, “멍청이”]
• #특정기호, 숫자, 알파벳 등"""



