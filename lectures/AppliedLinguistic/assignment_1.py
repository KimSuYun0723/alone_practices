import re

def openfile(file):
    f = open(file, 'r', encoding = 'utf-8')
    text = f.read()
    f.close()
    return text

def preprocessing(text):
    cleaned_text = text
    cleaned_text = cleaned_text.lower()
    cleaned_text = re.sub('[,.-:;?]', '', cleaned_text)
    cleaned_text = re.sub('-', '', cleaned_text)
    cleaned_text = re.sub('’', '\'', cleaned_text)
    cleaned_text = re.sub('\n+', ' ', cleaned_text)
    cleaned_text = re.sub('\s{2,10}', ' ', cleaned_text)
    return cleaned_text

def count_dict(cleaned_text):
    l_ = cleaned_text.split(" ") #Tokens
    s_  = list(set(l_)) #Types
    print(f"Types: {len(l_)}, Tokens: {len(s_)}")
    
    dic = {}
    for i in range(len(s_)):
        c = l_.count(str(s_[i]))
        dic[s_[i]] = c
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    
    print(f"Language Complxity: {len(s_)/len(l_) * 100}")
    return dic

# text1
text1 = openfile('C:/_SY/alone_practice/lectures/AppliedLinguistic/sample_1.txt')
cleaned_1 = preprocessing(text1)
dic1 = count_dict(cleaned_1)

for tup in dic1:
    print(f"{tup[0]}: {tup[1]}")


print("=====================================")
#text2
text2 = openfile('C:/_SY/alone_practice/lectures/AppliedLinguistic/sample_2.txt')
cleaned_2 = preprocessing(text2)
dic2 = count_dict(cleaned_2)

for tup in dic2:
    print(f"{tup[0]}: {tup[1]}")