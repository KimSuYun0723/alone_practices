print("===============5번문제=================")
class word_processing:
    #1-1
    def __init__(self, file):
        self.f = open(file, "r")
        self.data = self.f.read()
        self.f.close()
    
    #1-2
    def list_(self):
        self.data_l = self.data.replace(".","").replace("!","").replace(",","").replace("\"","").split(" ")
        return self.data_l
    
class identify_infl(word_processing):
    #2-2
    def up(self):
        self.inflec = input("Write the inflection form you want: ")
        self.data0 = self.data.split(" ")
        for i in range(len(self.data0)):
            if self.inflec in self.data0[i]:
                self.data0[i] = self.data0[i][:-len(self.inflec)] + self.data0[i][-len(self.inflec):].upper()
                print(self.data0[i])
        self.answer = " ".join(self.data0)
        return self.answer

a = identify_infl("story_short.txt")
data = a.list_()
up = a.up()
print(up)