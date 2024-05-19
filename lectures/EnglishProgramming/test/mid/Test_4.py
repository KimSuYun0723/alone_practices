review = """Sarah 4/5
I upgraded to the iPhone 14 and I'm absolutely loving it! The camera is amazing and the battery life is impressive. Definitely worth the investment.
John 5/5
The iPhone 14 is a great device, but I was expecting more upgrades compared to the previous model. Still, it's a solid choice if you're in need of a new phone.
Emma 4/5
I love the new design of the iPhone 14. It's sleek and feels great in my hand. The screen is also very vibrant and clear. Overall, very satisfied with my purchase.
Tom 4/5
I'm a big fan of Apple products and the iPhone 14 did not disappoint. The A15 Bionic chip makes everything run smoothly and the 120Hz ProMotion display is a game changer.
Lisa 5/5
I upgraded to the iPhone 14 from a much older model and I'm blown away by the improvements. The 5G connectivity is super fast and the camera takes stunning photos. Highly recommend!
Mike 2/5
I'm a huge fan of Apple products. I was really excited to upgrade to the iPhone 14, but I've been having some issues with the battery life. Even with minimal usage, it seems to drain faster than my old phone. It's frustrating to have to constantly worry about charging it."""

#1. 전체 리뷰의 평점을 구하고 출력
#/5 혹은 /를 찾아서 앞에 인덱스를(i-1)뽑아
#혹은 /를 기준으로 split 해서 0번 인덱스의 마지막 인덱스가 점수-> 이런 식으로
#나눌 때도 5로 나누는 사람도 있고, len 이나 /의 개수를 찾아서 나눈 사람도 상이하겠지

print("========== 1. ==========")
review01 = review
print(review01)
review01 = review01.split("\n")
print(review01)
review01 = review01[::2]
print(review01)
review01_str = " ".join(review01) 
review01 = review01_str.split(" ")
print(review01)
review01 = review01[1::2]
print(review01)
review01_str = "/".join(review01)
review01 = review01_str.split("/")
print(review01)
review_list = review01[::2]
a = '3'
b = int(a) #3
list = []
num01 = int(review_list[0])
num02 = int(review_list[1])
num03 = int(review_list[2])
num04 = int(review_list[3])
num05 = int(review_list[4])
num06 = int(review_list[5])
list.append(num01)
list.append(num02)
list.append(num03)
list.append(num04)
list.append(num05)
list.append(num06)

average = int(sum(list)/len(list))
print("평균 : ", average, "점")


#2. 이름과 점수만 추출
print("\n\n========== 2. ==========")
review02 = review
review02 = review02.split("\n")
review02 = review02[::2]
review02_str = " ".join(review02) 
review02 = review02_str.split(" ")
review02 = review02[::2] #이름만
print(review02[0],":", list[0])
print(review02[1],":", list[1])
print(review02[2],":", list[2])
print(review02[3],":", list[3])
print(review02[4],":", list[4])
print(review02[5],":", list[5])
#while을 쓰면 되잖아....



#3. review 부분만 review라는 이름의 list 변수에 담고 출력
print("\n\n========== 3. ==========")
review03 = review
review03_list = review03.split("\n")
print(review03_list)
real_list = review03_list[1::2]

list = []
list.append(real_list[0])
list.append(real_list[1])
list.append(real_list[2])
list.append(real_list[3])
list.append(real_list[4])
list.append(real_list[5])
print(list)
