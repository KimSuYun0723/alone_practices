print("==========5번문제==========")
class Stack:
    def __init__(self):
        self.stack_list = []
    def push(self, a):
        self.stack_list.append(a)
        return a
    def pop(self):
        if len(self.stack_list) != 0:
            a = self.stack_list.pop()
            return a
        else:
            raise IndexError 
    def peek(self):
        if len(self.stack_list) != 0:
            print(self.stack_list[-1])
    def __call__(self):
        print(self.stack_list)

data1 = "[({})]"
data2 = "[({])}"
data3 = "[({})"
print("1==============")
try:
    s = Stack()
    for d in data1:
        if d =="[":
            s.push(d)
            s()
        elif d =="]":
            s.pop()
            s()
    print("괄호의 짝이 모두 맞습니다.")
except IndexError:
    print("pop할 자료가 없습니다.")

print("2==============")
#2
try:
    s = Stack()
    for d in data2:
        if d =="[":
            s.push(d)
            s()
        elif d =="]":
            s.pop()
            s()
    print(s.stack_list)
    print("괄호의 짝이 맞지 않습니다.")
except IndexError:
    print("pop할 자료가 없습니다.")

print("3==============")
#3
try:
    s = Stack()
    for d in data3:
        if d =="[":
            s.push(d)
            s()
        elif d =="]":
            s.pop()
            s()
    print("괄호가 남았습니다.")
except IndexError:
    print("pop할 자료가 없습니다.")

