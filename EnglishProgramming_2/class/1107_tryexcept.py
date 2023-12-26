#3p
class file:
    def __init__(self, file):
        self.f = open(file, "r")
        self.d = self.f.read()
        self.f.close()
    
class text_pro(file):
    def t_split(self):
        result = self.d.split(" ")
        return result
    
    def __call__(self):
        print(self.t_split())

try:
    a = text_pro("hello1.txt")
    a()
except:
    print("ERROR")
    
#4p
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
    def __call__(self):
        print(self.add())
        print(self.sub())
        print(self.mul())
        print(self.div())
        
try:
    a = FourCal(4,2)
    a = FourCal(4,0)
    a()
except:
    print("0으로 나눌 수 없습니다!")
    
#5p
def write(file, data):
    f = open(file, "w")
    f.write(data)
    f.close()
    
try:
    write("test.txt", "abc")
except:
    print("Write Letters!")
    
#6p
class Fourcal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def div(self):
        result = self.first / self.second
        return result
    def __call__(self):
        self.div()
try:
    a = Fourcal(4, 0)
    a()
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다!")

try:
    a = FourCal(4, "a")
    print(a())
except TypeError:
    print("숫자를 입력하세요!")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다!")
    
try:
    a = FourCal("a", 0) #에러가 2갠데.. 첫번째 만나는 에러만 처리
    print(a())
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다!")
except TypeError:
    print("숫자를 입력하세요!")
    
class letter_counter:
    def __init__(self, word):
        self.word = word
    def counter(self):
        num_letter = len(self.word)
        print("The length of the word {0} is {1}".format(self.word, num_letter))
try:
    b = letter_counter(123)
    b.counter()
except TypeError as error:
    print("문자를 입력하세요! ({0})".format(error))
