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
print("========== 1. ==========")
data = review.split()

i = 0
list = []
while "/" not in data[i]:
    k = data.pop(i)
    print(k)
    i += 1
else:
    print("안빠져: ",data[i])
    i += 1
    print(i)

print(data)
