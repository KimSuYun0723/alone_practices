#이미 존재하는 별명_ 이것들을.. 객체로 만들 수도 있나...?
exist_nick = ["김수윤", "Kim", "KimSuYun", "SuYun", "sy"]

#허용하지 않는 문자열
disallow = ["바보", "stupid", "@", "fool"]
#disallow.extend(str(i) for i in range(10)) _ ListComprehension

class Already(Exception):
    def __str__(self):
        return "=== ERROR!! : 이미 있는 닉네임입니다. ==="

class NotAllowed(Exception):
    def __str__(self):
        return "=== ERROR!! : 허용되지 않은 단어가 닉네임에 있습니다. ==="

class Name:
    def __init__(self):
        nickname = input("별명을 입력하세요: ")
        self.nickname = nickname

    def confirm(self):
        if self.nickname not in exist_nick:
            self.nickname = self.nickname.lower() #허용되지 않은 단어는 대소문자 구별없이  
            for i in range(len(disallow)):
                if disallow[i].lower() in self.nickname:
                    raise NotAllowed()
                else:
                    if i == len(disallow)-1:
                        print("~닉네임이 성공적으로 입력되셨습니다~")
        else:
            raise Already()

repeat = True # 다시 입력하도록 반복할 수단
while repeat:
    try:
        a = Name()
        a.confirm()
        repeat = False #조건에 만족되면 종료
    except Already as error:
        print(error)
    except NotAllowed as error:
        print(error)