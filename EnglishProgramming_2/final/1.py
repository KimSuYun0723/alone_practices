print("==========1번문제==========")
class openfile:
    def __init__(self):
        self.file = input("파일을 입력하세요: ")
    def __str__(self):
        return self.file
    def openf(self):
        f = open(self.file, "r")
        self.data = f.read()
        if self.data == "":
            raise myerror1
        f.close()
        return self.data
class myerror1(Exception):
    def __str__(self): 
        return "No such file or directory : " 

try:
    a = openfile()
    a.openf()
except UnicodeDecodeError as error:
    print("파일의 인코딩을 다시 확인하세요! \n{0}".format(error))
except myerror1 as error:
    print("파일 이름과 파일 위치를 다시 확인하세요 \n{0}{1}".format(error, "file_open1.txt"))


















