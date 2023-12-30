print("===============4번문제=================")
def word_processing(file, inflec):
    #2-1
    def file_read():
        f = open(file, "r")
        data = f.read()
        f.close()
        return data
    
    #2-2
    def list_(data):
        data_l = data.replace(".","").replace("!","").replace(",","").replace("\"","").split(" ")
        return data_l
    
    #2-3
    def up(data):
        data0 = data.split(" ")
        for i in range(len(data0)):
            if inflec in data0[i]:
                data0[i] = data0[i][:-len(inflec)] + data0[i][-len(inflec):].upper()
                print(data0[i])
        answer = " ".join(data0)
        return answer
    
    data = file_read()
    list_(data)
    print(up(data))
    
word_processing("story_short.txt", "ed")