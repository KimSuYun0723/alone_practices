#oop2
#6p-containment
class A:
    def methodA(self):
        print("yes")   
class B:
    def __init__(self):
        self.instance_of_A = A()
    def call_methodA(self):
        self.instance_of_A.methodA()

Classb = B()
Classb.call_methodA()

#8p- super()
class A:
    def __init__(self):
        print("A클래스의 init이 실행됨")
        self.message = "HEllo"
class B(A):
    def __init__(self):
        print("B클래스의 init이 실행됨")
        super().__init__()
        print("super()을 통해 A클래스의 __init__ 호출 "+ self.message)
        
b = B()

#10p-static & class method 비교_상속
#static method
class Parent:
    name = "Mary"

    @staticmethod
    def change_name(new_name):
        Parent.name = new_name

class Child(Parent):
    pass

parent = Parent()
child = Child()
parent.change_name("Jane") #Jane, Jane
print(f"부모 클래스로 호출하면: parent-{parent.name} child-{child.name}")
parent = Parent()
child = Child()
child.change_name("Ann") #Ann, Ann
print(f"자식 클래스로 호출하면: parent-{parent.name} child-{child.name}")


#class method
class Parent:
    name = "SuYun"

    @classmethod
    def change_name(cls, new_name):
        cls.name = new_name

class Child(Parent):
    pass

parent = Parent()
child = Child()
parent.change_name("Jane") #Jane, Jane
print(f"부모 클래스로 호출하면: parent-{parent.name} child-{child.name}")
parent = Parent()
child = Child()
child.change_name("Ann") #!!!!Jane!!!!, Ann
print(f"자식 클래스로 호출하면: parent-{parent.name} child-{child.name}")
#자식 클래스에서 parent.name --> Ann으로 안바뀜. 그대로 Jane.

#method overriding

#__call__()
class Callable:
    def __call__(self):
        print("I am called")
        
obj = Callable()
obj()

#22p - 실습
#텍스트 파일을 open & read하는 부모 클래스
class File:
    def __init__(self,file):
        f = open(file, "r")
        self.data = f.read()
        f.close()
#상속을 이용하여 텍스트 파일을 단어로 split하는 자식 클래스
class Word(File): #다양한 방법의 상속을 실습해 볼 것
    def data2word(self):
        self.word = self.data.split(" ")
        print(self.word) 
    #위 내용에 __call__ method 추가
    #단어로 split하는 함수 호출 및 출력
    def __call__(self):
        self.data2word()

a = Word("C:\pythonpractice\EnglishProgramming_2\data\story_short.txt")
a()













