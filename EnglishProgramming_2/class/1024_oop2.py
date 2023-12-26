#정적 메소드 - self 없이 사용하는 애들
#클래스 메소드 _cls 라는 매개변수 달고 다녀야한다
class Fourcal:
    @staticmethod
    def plus(a,b):
        return a+b


#31p
class InstanceCounter:
    count=0

    def __init__(self):
        self.c = 0
        InstanceCounter.count+=self.c

    @classmethod
    def print_instance_count(cls):
        print(cls.count)
    
a = InstanceCounter()
InstanceCounter.print_instance_count()
b = InstanceCounter()
InstanceCounter.print_instance_count()
c = InstanceCounter()
c.print_instance_count()

#33p- instance method
class wordlen2:
    def __init__(self, word):
        self.w = word

    def length(self):
        w_len = len(self.w)
        return w_len

#static method
class len_word:
    @staticmethod #init 필요없음, 그냥 함수랑 똑같은거임 사실 이 상황에서는 static을 써야 하는 문제는 아니다
    def length(word): #static이라서 self없이 바로 word
        return len(word)
print(len_word.length("lion"))

#class_method
class wordlen3:
    c="김수윤"
    
    def __init__(self): #얘도 굳이 count안해줄 상황이면 필요한 것인가?
        self.c +=1
        print(self.c) #cls.c랑 얘랑 다른 c인것 같음.
        wordlen3.c +=1 #cls라는 매개변수는 없으니까 안되고, 클래스 이름을 써야함
                        # 근데.. 이렇게 클래스 이름으로 쓰는건, classmethod안쓸 때도 가능한것이 아닐..까?

    @classmethod
    def length(cls, word): #cls를 안쓰면 굳이 cls가 남아있어야 하나!!?
        p = f"{wordlen3.c}-{word}: {len(word)}"
        p = f"{cls.c}-{word}: {len(word)}" #위아래 다 똑같은거임.
        return p
    
a = wordlen3()
print(wordlen3.length("lion"))
b = wordlen3()
print(wordlen3.length("mango"))

#이것도 가능
"""
class wordlen3:
    c="김수윤"
    @classmethod
    def length(self): 
        p = f"{wordlen3.c}"
        return p
    
a = wordlen3()
print(a.length())
"""

########################################################
#상속
class Base:
    def base_method(self):
        print("base_method")

class Derived(Base):
    pass

a = Derived()
a.base_method()


#실습 4p
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
    
class MoreFourcal(FourCal):
    def power(self):
        result = self.first ** self.second
        return result

a = MoreFourcal(2,3) #엄마한테 init 있으니까 엄마꺼에 써도돼
print(a.power())
print(a.add()) #엄마꺼도 가능

class op:
    def __init__(self, file):
        self.file = file
    def r(self):
        self.f = open(self.file, "r")
        data = self.f.read
        return data
    
class sp(op):
    def divide(data):
        text = str(data).replace(",", "").replace(".", "").replace("'s", " 's").replace("\"", "").replace("\n", " ").lower()
        answer = text.split(" ")
        return answer
    
a = sp("TheNorthWind&theSun.txt")
print(a.divide())

#professor
class file:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, "r")
        self.d = self.f.read()
    
class text_pro(file):
    def t_split(self):
        result = self.d.split()
        return result
    
a = text_pro("TheNorthWind&theSun.txt")
print(a.t_split())


#클래스의 상속
class A:
    def methodA(self):
        print("yes")
    
class B:
    def __init__(self):
        self.instance_of_A = A() #클래스 B를 생성하는 순간 A호출 , A라는 클래스의 객체 이름
    def call_methodA(self):
        self.instance_of_A.methodA()


Classb = B() #일단 객체 생성 -> init ->A 클래스 객체 생성
Classb.call_methodA() #호출 -> A객체 갖고 와서 methodA가 나오는 것.


#super
class A:
    def __init__(self):
        print("A 클래스의 __init__()이 실행됨")
        self.message = "Hello"

class B(A):
    def __init__(self):
        print("B 클래스의 __init__()이 실행됨")

        super().__init__()
        print("super()통해 A 클래스의 __init 호출"+self.message)

b = B()
#자식클래스와 부모 클래스 2개다 생성자가 있으면 하나만 실행됨
#엄마꺼는 실행이 안되고, 엄마꺼를 실행시킬 다른 장치가 필요하다!
#containment까지