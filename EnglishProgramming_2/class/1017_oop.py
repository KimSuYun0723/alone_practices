class FourCal:
    def __init__(self, first, second): #객체를 생성하는 지점에 바로 변수를 활용해줘야함. 아니면 에러남
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    
def cal(first, second):
    #first=first
    #second=second
    def add():
        print(first+second)

    add()

cal(1,2)
a = cal(1,2)


#단어의 길이 즉, 글자수 세는 클래스를 만들어보자
class word:
    def __init__(self, data):
        self.data = data

    def c(self):
        if "," in self.data:
            data = self.data.replace(",", "").split(" ")
            for i in data:
                print(len(i))
        else:
            c = len(self.data)
            print(c)

one = word("lion")
one.c()
two = word("pple, pear, melon, orange, kiwi")
two.c()

#단어, 단어의 빈도, 단어의 길이, 종류를 list에 입력하고 출력하는 word_info 클래스
class word_info:
    def __init__(self, word, wordf, wordl, wordt) :
        self.word = word
        self.wordf = wordf
        self.wordl = wordl
        self.wordt = wordt

    def p(self):
        l = []
        l.append(self.word)
        l.append(self.wordf)
        l.append(self.wordl)
        l.append(self.wordt)
        for i in l:
            print(i)

ant = word_info("ant", "5.347108", "3", "animal")
ant.p()

class op:
    def __init__(self, file):
        self.file = file

    def r(self):
        self.f = open(self.file, "r")
        self.data = self.f.read()
        self.f.close()
        return self.data
    
class sp(op):
    def divide(self, data):
        self.text = str(self.data).replace(",", "").replace(".", "").replace("'s", " 's").replace("\"", "").replace("\n", " ").lower()
        self.answer = self.text.split(" ")
        print(self.answer)
    
a = sp("C:\\pythonpractice\\EnglishProgramming_2\\test\\TheNorthWind&theSun.txt")
data = a.r()
a.divide(data)


def cal(first, second):
    #first=first
    #second=second
    def add():
        return first+second
    add() #return은 되었으나 받아주는 변수가 없음

a = cal(1,2)
print(a) #add 함수안에는 return이 있지만, cal 함수에는 리턴이 없고 & 

class init_test:
    def __init__(self, a, b): #a,b가 필요하다고 했는데
        print("객체생성")

test = init_test(1,2) #호출할때 안넣으면 에러가 남.


class postag:
    def __init__(self, word, pos):
        self.word = word
        self.pos = pos

    def print_info(self):
        print('{0} : {1}'.format(self.word, self.pos))

apple = postag('apple', 'noun')
eat = postag('eat', 'verb')

apple.print_info()
eat.print_info()

class text_appending:
    text_list = []

    def add(self, text):
        self.text_list.append(text)

    def print_list(self):
        print(self.text_list)

a = text_appending()
a.add("a")
a.print_list()
b = text_appending()
b.add("b")
b.print_list()


class text_appending:
    def __init__(self):
        self.text_list = []

    def add(self, text):
        self.text_list.append(text)

    def print_list(self):
        print(self.text_list)

a = text_appending()
a.add("a")
a.print_list()
b = text_appending()
b.add("b")
b.print_list()


class Fourcal:
    @staticmethod
    def plus(a,b):
        return a+b

Fourcal.plus(1,2)
a = FourCal(1,2)
print(a)
#차이가 뭘까? 그냥이랑, 객체 만든거랑 --> 변수를 새로 만드느냐 안만드느냐의 차이.

#Containment()
class A:
    def methodA(self):
        print("yes")

class B:
    def __init__(self):
        self.instance_of_A = A()
    def call_methodA(self):
        self.instance_of_A.methodA()


#정적 메소드
class word_length1:
    @staticmethod
    def length(word):
        leng = len(word)
        print("length is",leng)

word_length1.length("lion")

#클래스 메소드 실습
class word_length2:
    count = 1

    @classmethod
    def length(cls, word):
        cls.leng = len(word)
        print("length is",cls.leng, word_length2.count)
        word_length2.count += 1

word_length2.length("apple")
word_length2.length("mago")
word_length2.length("gogogo")


