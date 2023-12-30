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
    
    if type(data) == str:
        str_w()
    elif type(data) == list:
        list_w()
    

a = 'write test 1'
file_write('write_test1.txt', a)
b = ['write', 'test', '2']
file_write('write_test2.txt', b)