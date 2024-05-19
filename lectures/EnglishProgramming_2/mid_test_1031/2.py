print("===============2번문제=================")

def file_write(fname, data):
    f = open(fname, "w")
    data0 = data[::]
    for i in range(len(data0)):
        data0[i] = str(data0[i])
    f.writelines(data0, end = " ")
    f.close()

data = [2023,10,31,"midterm", "exam"]
file_write("file_write_test_김수윤.txt", data)
