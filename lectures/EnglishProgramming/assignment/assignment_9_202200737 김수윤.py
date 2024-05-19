"""
• file_write 함수 안에 아래 두개 함수를 중첩해서 넣기
• file_write의 매개변수는 1. 파일이름, 2. 데이터(문자열/리스트)
• str_w 함수: 데이터가 문자열일때 파일에 쓰는 함수
• list_w 함수: 데이터가 리스트일때 파일에 쓰는 함수
• test run
• a = “write test 1”
• file_write(“write_test1.txt”, a)
• b = [“write”, “test”, “2”]
• file_write(“write_test2.txt”, b)
"""
#매개변수에 data_type도 변수로 받아서 하지말고 함수 내에서 따로 처리하세요
def file_write(file, data):
    f = open(file, "w")

    def str_w():
        f.write(data)
        f.close()
        print(data)

    def list_w():
        data1 = ".".join(data)
        f.write(data1)
        f.close
        print(data1)
    
    #def data_type()
    if type(data) == str:
        str_w()
    elif type(data) == list:
        list_w()
    #data_type()

file_write("file_write_test1.txt", "abc")
file_write("file_write_test2.txt", ["a", "b", "c"])