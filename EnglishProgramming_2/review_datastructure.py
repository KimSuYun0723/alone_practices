#괄호 검사


#회문 검사
class Stack:
    def __init__(self):
        self.stack_list = []
    def push(self, a):
        self.stack_list.append(a)
        print(a,"inserted") 
    def pop(self):
        if len(self.stack_list) != 0:
            a = self.stack_list.pop()
            print(a, "deleted")
        else:
            raise IndexError
    def peek(self):
        if len(self.stack_list) != 0:
            return self.stack_list[-1]
    def __call__(self):
        print(self.stack_list)


data = "abcTcba"
try: 
    s = Stack()
    standard = len(data)
    for i in range(int(standard/2)):
        s.push(data[i]) #스택에 앞에 3개 넣음 abc --> c,b,a
        print(s.stack_list)
        
    if standard%2==0:
        print("짝수인 경우")
        for i in range(int(standard/2)):
            front = s.pop() #a-b-c
            print(front)
            if front == data[standard-i]:
                continue
            elif front != data[standard-i]:
                raise Exception()
            if i == int(standard/2)-1:
                print("회문입니다!!!")
                


except IndexError:
    print("스택이 비었어요")
except Exception:
    print("회문이 아니에요!!!")



"""data = "abcTcba"
try: 
    s = Stack()
    
    l = len(data)
    l_ = len(data)/2
    
    for i in range(len(data)):
        if i < l_:
            s.push(data[i])
            s()
        else:
            if s.peek() == data[i]:
                s.pop()
                s()
except IndexError:
    print("Pop from an empty")  """
    
