#Open and read file "TheNorthWind&theSun.txt"
def openf(file):
    f = open(file, "r")
    data = f.read()
    f.close()
    return data

#Make words list(NOT repeated)
def words_set_list(data):
    clean = data.replace("\n", " ").replace(",", "").replace(".", "").replace("\"", "").replace("\'s", "").lower() #'s를 " 's"로 바꾸면 보존 가능
    words_set = sorted(list(set(clean.split(" ")))) #sorted는 자동으로 list로 바꿔주기 때문에 원래는 list 안써도되지만 explicit하게
    return words_set

#Make data list(Repeated)
def words_list(data):
    clean = data.replace("\n", " ").replace(",", "").replace(".", "").replace("\"", "").replace("\'s", "").lower()
    words = clean.split(" ")
    return words

#Make dictionary
def make_dict(words_set, words): #딕셔너리가 아닌 단어로 loop을 돌면서 해야 순서가 지켜짐
    dict = {}
    for i in words_set:
        c = words.count(i)
        dict[i] = c
    return dict

#Using functions
data = openf("TheNorthWind&theSun.txt")
words_set = words_set_list(data)
words = words_list(data)
dict = make_dict(words_set, words)

#원래는 딕셔너리에 중복제거한 단어를 넣을 때부터 정렬된 단어를 집어넣으려고 했지만,
#깔끔하게 딕셔너리를 아예 만들고 정렬하는 것이 예외가 없겠다 싶어 딕셔너리 key를 기준으로 정렬.
tup  = sorted(dict.items())

#Create file "wind_sun_w_freq.txt" to write on
f2 = open("wind_sun_w_freq.txt", "w")

#Student ID & Name
f2.write("====== 202200737 SuYunKim ======\n\n") 

for i in tup:
    if i == tup[-1]:
        #맨 마지막줄에 \n가 들어가는 경우를 조정해줌.
        f2.write(f"{i[0]} : {i[1]}")
    else:
        f2.write(f"{i[0]} : {i[1]}\n")

f2.close()