word = str(input("찾을 단어를 입력하세요: "))
List = [f"{word}", f"{word}s", f"{word}ed", f"{word}ing"]

def reg_verb_finder(file, word):
    def file_reader(file):
        f = open(file, "r")
        text = f.read()
        f.close()
        return text
    
    def data_cleaner(text):
        text = text.replace(".", " ").replace("\n", " ").replace(",", " ").replace("\'s", " ")
        text = text.replace("  ", " ").rstrip()
        return text
    
    def Print(word, text):
        num=0
        total = 0
        c = []
        words = text.lower().split(" ") 
        for i in List:
            for j in words:
                if i == j:
                    num+=1
                c.append(num)
                total += num
                print(f"The frequency of the verb \"{word}\"is {total}")
        for i in len(c):
            print(f"{word[i]}: {c[i]}")

    file_reader()
    data_cleaner()
    Print()
    
reg_verb_finder("walk.txt", word)
                

