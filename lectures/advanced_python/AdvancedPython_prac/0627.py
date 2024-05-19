"""
• 자신의 이름과 학번을 활용하여 이름: 학번 형태로 출력하기
• 예) JiwonJang: 12345678
• 변수 name에 자신의 이름을, num_id에 자신의 학번 넣기
• 이름과 학번을 직접 입력하지 말고, 변수 이름을 사용해서 출력하기 (print 함
수 사용)
"""

name = input("이름을 입력하세요 \n: ")
num = input("학번을 입력하세요 \n: ")

print(str(name)+":", str(num))
print(str(name)+":", int(num))
print(str(name)+": "+int(num)) #error
