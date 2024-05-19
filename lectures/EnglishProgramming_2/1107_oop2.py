"""
부모, 자식 클래스 둘다 init이 있으면
자식클래스 생성자만 실행.
부모클래스의 메소드를 가져오려면
super() 사용
super().__init__()이렇게
----
둘 중 하나만 생성자 --> 그거 실행
----
상속 배울 때는 변수만 가져와서 썼었음.
지금은 메소드를 가져와서 쓰는거고.
부모 자식 둘다에 생성자가 있는게 아니면 그냥 self.가져와서 쓸 수 있지만
super().method()가 되면 객체를 가져올 수 있는게 아님

"""
#7p 실습1
class A:
    def __init__(self):
        print("A 클래스 생성자 실행")
        self.message = "Hello"
        
    def hi(self):
        print("HI")
        
class B(A):
    def __init__(self):
        print("B 클래스 생성자 실행")
        
        super().__init__()
        super().hi() 
        print("super()통해 A클래스의 생성자 호출"+self.message)

b = B()

#7p 실습 2
class A:
    def __init__(self):
        print("A 클래스 생성자 실행")
        self.message = "Hello"
        
    def hi(self):
        print("HI")
        
class B(A):
    def hihi(self):
        print("B hihi 실행")
        
        super().__init__()
        super().hi() 
        print("super()통해 A클래스의 생성자 호출"+self.message)

b = B()

#
class A:        
    def hi(self):
        print("HI")
        
class B(A):
    def __init__(self):
        print("B 클래스 생성자 실행")
        self.hi() #자식클래스에 호출을 해서 뭔가를 해야할 때 쓰지, 이렇게 간단하게 쓰면 self.hi()랑 똑같겠지

b = B()

#static vs class method
#클래스 메소드를 통해서 자식 클래스로 호출하면, 부모클래스 내용은 안바뀌고 자식껏만 바뀌는구나
class Parent:
    name = 'Mary'
    @staticmethod
    def change_name(new_name):
        Parent.name = new_name
class Child(Parent):
        pass

class Parent:
    name = 'Jiwon'
    @classmethod
    def change_name(cls, new_name):
        cls.name = new_name
class Child(Parent):
        pass

parent = Parent()
child = Child()
parent.change_name("Jane")
print(f"부모클래스로 호출하면 : parent-{parent.name} child - {child.name}")

print("=======================")
parent = Parent()
child = Child()
child.change_name("Ann")
print(f"자식클래스로 호출하면: parent-{parent.name} child- {child.name}") #

#method_overriding
class FourCal:
    def __init__(self, first, second): #객체를 생성하는 지점에 바로 변수를 활용해줘야함. 아니면 에러남
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def div(self):
        self.result = self.first / self.second
        return self.result

"""a = FourCal(4,0)
print(a.div()) #에러남. 분모가 0이라서"""

class SafeFourcal(FourCal):
    def div(self):
        if self.second ==0:
            return "두번째 숫자가 0입니다"
        else:
            super().div()
            return self.result
        
a = SafeFourcal(4,5)
print(a.div())
#근데... self 다똑같으면 다 같은 객체인건가..?

#15p
class word_pos:
    def pos(self, word):
        print(word)
        print("noun")

class appen_pos(word_pos): # 부모 class 상속
    def pos(self, word): # overriding 재정의
        super().pos(word) # super()를 통해 부모 클래스 메소드 호출
        print("verb") # overriding 통해 자신만의 기능을 덧붙임
 
email = appen_pos()
email.pos("email") #email noun verb

email = word_pos()
email.pos("email") #email noun 

#Overloading
class SampleA():
    def add(self, datatype, *args):
        if datatype =='int':
            return sum(args)
        if datatype == 'str':
            return ''.join([x for x in args]) #앞에 x에 args가 다 들어있는거임

a = SampleA()
print('SampleA > ', a.add('int', 5,6,3))
print('SampleA > ', a.add('str', "Hello", "World"))

# 18p 실습 하는데 교수님이 super 쓰는데 __init_안에 안쓰고 그냥 슈퍼로 불러오니까 런타임 에러 뜸 뭘까?
class A:
    def a(self):
        print("A")
class B:
    def b(self):
        print("B")
class C:
    def c(self):
        print("C")
class D(A,B,C):
    def __init__(self):
        super().a()
        super().b()
        super().c()
d=D() #이게 없으면 호출이안되니까

#__call__
class Callable:
    def __call__(self):
        print("I am called")

obj = Callable()
obj()

#실습
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
        
a = FourCal(1,2)

#22p 실습
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
    
a = text_pro("hello.txt")
a()

