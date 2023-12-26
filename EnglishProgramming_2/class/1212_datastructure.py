#Stack
class Stack:
    def __init__(self):
        self.stack_list = []
    def push(self, a):
        self.stack_list.append(a)
        print(a,"inserted")
    def pop(self):
        a = self.stack_list.pop()
        print(a, "deleted")
    def __call__(self):
        print(self.stack_list)
        
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s()

#스택 오류처리
print("\n\n\n====스택 오류 처리====")
class Stack1:
    stack_limit = 3
    def __init__(self):
        self.stack_list = [] 
    def push(self, a):
        if len(self.stack_list) < Stack1.stack_limit:
            self.stack_list.append(a)
            print(a,"inserted")
        else:
            print("Stack Overflow!")
    def pop(self):
        if len(self.stack_list) != 0:
            a = self.stack_list.pop()
            print(a, "deleted")
        else:
            print("Stack Empty!")
    def __call__(self):
        print(self.stack_list)
        
s = Stack1()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s()
s.pop()
s.pop()
s.pop()
s.pop()
s()

#오류 처리 2
print("\n\n====오류 처리2====")
class Stack2:
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
            raise IndexError #이걸로 예외처리하는게 더 예쁘겠지
    def peek(self):
        if len(self.stack_list) != 0:
            print(self.stack_list[-1])
    def __call__(self):
        print(self.stack_list)

try:
    s = Stack2()
    s.push(1)
    s.push(2)
    s.push(3)
    s.peek()
    s()
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s()
except:
    print("pop할 자료가 없습니다.")
finally:
    s()
    
#괄호 검사
#근데 괄호 하나 더 넣었나봐... indexerror에 걸렸어
data = """[S
    [NP
        [Det The]
        [N child]
    ]
    [VP
        [V drew]
        [NP 
            [Det an] 
            [N elephant]
        ]
    ]
]
"""
try:
    s = Stack2()
    for d in data:
        if d =="[":
            s.push(d)
            s()
        elif d =="]":
            s.pop()
            s()
except IndexError:
    print("pop할 자료가 없습니다.")

#회문 검사하기
print("\n\n\n회문검사~~~~~~")
data = input("회문 검사할 스트링 : ")
try: 
    s = Stack2()
    for i in range(int(len(data))):
        s.push(data[i])
        
    if len(data)%2==0:
        for i in range(len(data), int(len(data)/2)+1, -1):
            compare = s.pop()
            if compare == data[i]:
                continue
            elif compare != data[i]:
                raise IndexError()
                
    elif len(data)%2 !=0:
        for i in range(len(data), int(len(data)/2)+1, -1):
            compare = s.pop()
            if compare == data[i]:
                continue
            elif compare != data[i]:
                raise IndexError()
except IndexError:
    print("회문이 아니에요!")
    
        
#Queue
class Queue:
    def __init__(self):
        self.queue_list = []
    def enqueue(self, a):
        self.queue_list.append(a)
        print(a,"inserted")
    def dequeue(self):
        a = self.queue_list.pop(0)
        print(a, "deleted")
    def __call__(self):
        print(self.queue_list)

s = Queue()
s.enqueue(1)
s.enqueue(2)
s.enqueue(3)
s()
s.dequeue()
s.dequeue()
s.dequeue()
s.dequeue()
s()

# 전방 탐색 할때... ?를 쓰는거랑 (?=*)가 뭐 충돌이 있음. 그래서 전방 탐색이랑 몇개 중에 1개만 써야 해서 AB+가 아니라 ABAB 이렇게 그냥 써줘야해
    
#큐의 오류처리
print("\n\n큐의 오류처리 ==========")
class Queue1:
    queue_limit = 3
    def __init__(self):
        self.queue_list = []
    def enqueue(self, a):
        if len(self.queue_list) < Queue1.queue_limit:
            self.queue_list.append(a)
            print(a,"inserted")
        else:
            print("Queue Overflow!")
    def dequeue(self):
        if len(self.queue_list) != 0:
            a = self.queue_list.pop(0)
            print(a, "deleted")
        else:
            print("Queue Empty!")
        def __call__(self):
            print(self.queue_list) 
            

#limit없애고 dequeue만 남김
class Queue2:
    def __init__(self):
        self.queue_list = []
    def enqueue(self, a):
        self.queue_list.append(a)
        print(a,"inserted") 
    def dequeue(self):
        if len(self.queue_list) != 0:
            a = self.queue_list.pop(0)
            print(a, "deleted")
        else:
            print("Queue Empty!")
    def __call__(self):
        print(self.queue_list) 
        
#큐는 언어 관련해서 뭐 할게 없어. 회문검사랑 트리 연습하는거는 스택이 더 할만한 듯
#짝수 홀수 그거는 꼭 연습해보고!(스택 관련해서), 트리도 실습하면 좋을듯
