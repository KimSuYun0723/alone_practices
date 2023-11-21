#상대경로가 안될 떄는 대체로 같은 파일이름인데 다른 경로로 저장되어있는 경우
#그럴 때는 .txt파일과 같은 경로에 다시 저장
#close한 파일은 다시 access 불가.

"""
f=open("TheNorthWind&theSun.txt", "r")
data = f.read()
print(data)
f.close()

f=open("TheNorthWind&theSunWrite.txt", "w")
f.write("hello")
f.close()

f=open("TheNorthWind&theSunX.txt", "x") #절대경로에서 당연히 에러고, 상대경로에서 에러
f.close()

f=open("TheNorthWind&theSunWrite.txt", "a")
f.write("!!!!!")
f.close()

f=open("TheNorthWind&theSun.txt", "r")
wind_sun = f.readline()
text = ""
while wind_sun != "":
    text += wind_sun
    wind_sun = f.readline()
print(text)
f.close()


#write
f=open("TheNorthWind&theSun.txt", "r")
data = f.readline()

data0 = data.replace("")

f.close()
"""

lines = ['안녕하세요?\n', 'こんにちは\n','Hello.\n']
with open('greetings_utf8.txt', 'w', encoding='utf-8') as file:
    for line in lines:
        file.write(line)

with open('greetings_utf8.txt', 'r', encoding='ascii', errors = "ignore") as file:
    lines = file.readlines()
    line = ''
    for line in lines:
        print(line, end='')
#errors = "ignore" -> 에러나도 할 수 있는 것만 프린트
#utf-16 다음번 시간에