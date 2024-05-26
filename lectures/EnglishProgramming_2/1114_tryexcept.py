#try_except_else
test_list = [0, 1, 2, 3, 4]
try:
    print("인덱스 번호를 입력하세요")
    index = int(input())
    result = index[index] #오류가 나는게 있어야 넘어감
except IndexError as error:
    print("인덱스 값에 오류가 있습니다! ({0})".format(error))
else: #while-else처럼 else 부분 인덴테이션 땡기면 안됨. 인덱스에 오류가 없더라도 오류가 한번 더 날 수 있기 때문에
    print("입력한 인덱스에 담겨 있는 값은", result)
    #하지만 finally는 가능하겠지.(땡겨쓰면 항상 실행되니까)
    #그럼 이걸 왜 만들었냐? --> 가독성
finally:
    print("프로그램 실행이 완료되었습니다.")
    
#오류 회피 -> 그냥 pass 쓰는거

#오류 일부러 발생시키기
try:
    raise Exception ("예외를 일으켜")
except Exception as err:
    print("예외발생! ({0})".format(err))

#raise Exception("ERROR") #Exception : Error
    #raise 써도 try except 가능

#오류 발생시키는 이유
class letter_counter:
    def __init__(self, word):
        self.word = word
    def counter(self):
        num_letter = len(self.word)
        print("The length of the word {0} is {1}".format(self.word, num_letter))

try:
    b = letter_counter("apple", "pear") #argument 2개 넣어서 에러 & 문자열이어서 에러
    b.counter()
except TypeError as error: #둘다 타입에러라 하나는 안걸려
    print(f"문자를 입력하세요: ({error})")
except TypeError as error:
    print(f"한 단어만 입력하세요! ({error})")
    
class letter_counter:
    def __init__(self, word):
        if int(word):
            raise Exception("단어를 입력하세요! ")
        else:
            self.word = word
    def counter(self):
        num_letter = len(self.word)
        print("The length of the word {0} is {1}".format(self.word, num_letter))
        
try:
    b = letter_counter("apple", "pear") #argument 2개 넣어서 에러 & 문자열이어서 에러
    b.counter()
except Exception as error: #모든 에러를 처리하는애라, TypeError도 포함. # 위아래 순서를 바꿔야함
    print(f"예외가 발생하였습니다.: ({error})")
except TypeError as error:
    print(f"한 단어만 입력하세요! ({error})")

#26p 실습
class letter_counter:
    def __init__(self, word):
        if int(word):
            raise Exception("숫자가 입력됨")
        elif " " in word:
            raise TypeError("두 단어가 입력됨")
        else:
            self.word = word
    def counter(self):
        num_letter = len(self.word)
        print("The length of the word {0} is {1}".format(self.word, num_letter))

try:
    c = letter_counter("apple pear") #예외발생1
    c.counter()
except TypeError as error:
    print(f"예외발생1 ({error})")
except Exception as error: 
    print(f"예외발생2 ({error})")

#사용자 정의 예외
class MyError(Exception):
    def __init__(self):
        super().__init__("Myerror가 발생합니다")

#raise MyError() #빨간글씨
try:
    raise MyError()
except:
    print("예외발생") #try except 넣으면 더이상 빨간글씨로 에러가 뜨진 않음
else:
    print("예외 발생 안함")

#28p-29p
class myerror_(Exception):
    def __str__(self): #str을 반환하는 메소드, 클래스 생성시 자동 실행
        return "글자를 입력하세요"
    
class letter_counter:
    def __init__(self, word):
        if int(word):
            raise myerror_()
        elif " " in word:
            raise Exception("한 단어만 입력해라")
        else:
            self.word = word
    def counter(self):
        num_letter = len(self.word)
        print("The length of the word {0} is {1}".format(self.word, num_letter))

try:
    c= letter_counter("123")
    c.counter
except myerror_ as error: 
    print("숫자 입력함", error)
except TypeError as error:
    print("argument 2개", error)
except Exception as error: #띄어쓰기 포함해서 2개
    print("단어 2개", error)
    
#__str__ 배울 때 _담을 수 없는걸 담아서 에러 뜸... print를 return 으로 바꿨더니 됨 뭐지?

#30p
dic = {"abnormal": "adjective", "adhere": "verb", "ant": "noun", "apple": "noun"}

class search_error:
    def __str__(self):
        return "사전에 단어가 없습니다."

class diction:
    def __init__(self):
        word = input("검색할 단어 입력 : ")
        self.word = word


try:
    w = diction()
    if dic[w.word]:
            print("사전에 단어가 존재합니다.")
except KeyError:
    e = search_error()
    print(e)
    
#30p - prof
class myerror(Exception):
    def __str__(self):
        return "사전에 존재 노노"
    
def dic_look_up():
    word = input("검색 단어 : ")
    if word in dic:
        print(word, ":", dic[word])
    else:
        raise myerror() #실행 중에 myerror를 실행하게 되면

try:
    dic_look_up()
except myerror as err: #여기로 넘어오게
    print(err)

            
            


