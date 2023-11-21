print("===============3번문제-verB=================")
#1
def file_read(file):
    f = open(file, "r")
    data = f.read()
    f.close()
    return data

#2
def w_l(data):
    clean = data.replace("\n", " ").replace(",", "").replace(".", "").replace("\"", "").replace("\'s", "").lower().split(" ")
    return clean

#3
def stopw(file):
    f = open(file, "r")
    data = f.read()
    stopw = data.split("\n")
    f.close()
    return stopw

#4
def freq(clean, stopw=None, num=10):
    if stopw != None:
        stopw_set = set(stopw)
        w_set0 = set(clean)
        w_set_0 = w_set0 - stopw_set
        w_set = sorted(list(w_set_0))
    else:
        w_set = sorted(list(set(clean)))
    dict = {}
    for i in w_set:
        c = clean.count(i)
        dict[i] = c
    
    
    tup  = sorted(dict.items(), key=lambda x:x[1], reverse=True)

    k=1
    while (k <= num):
        for i in tup:
            print(f"{i[0]} : {i[1]}")
            k+=1

#5
data = file_read("C:\\pythonpractice\\EnglishProgramming_2\\mid_test_1031\\story_long.txt")
clean = w_l(data)
stop = stopw("C:\\pythonpractice\\EnglishProgramming_2\\mid_test_1031\\nltk_stopword.txt")

#4번함수
print("순위 지정=========")
freq(clean, num=5)
print("순위 지정X=========")
freq(clean)
print("stop O=========")
freq(clean, stopw=stop)
print("stop X=========")
freq(clean)