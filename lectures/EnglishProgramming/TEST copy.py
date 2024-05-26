def cal(a, b):
    def cal_plus ():
        return a+b
    def cal_minus ():
        return a-b
    print(cal_plus())
    print(cal_minus())
cal(4,2)