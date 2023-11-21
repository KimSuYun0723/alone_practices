print("==========4번 문제==========")
data1 = "The stunning canvas of the twilight sky was adorned with the radiant hues of the descending sun."
data2 = "The resplendent colors of the setting sun adorned the twilight sky like a beautiful painting."

data = data1.replace(".", "").lower()
data1_list = list(set(data.split(" ")))

ex = data1_list[:]

data0 = data2.replace(".", "").lower()
data2_list = list(set(data0.split(" ")))

ex.extend(data2_list)
ex_s = sorted(ex)
#print(ex_s) #of, sky, sun, the, twilight

List = ["of", "sky", "sun", "the", "twilight"]

data1_list.remove(List[0])
data1_list.remove(List[1])
data1_list.remove(List[2])
data1_list.remove(List[3])
data1_list.remove(List[4])

data2_list.remove(List[0])
data2_list.remove(List[1])
data2_list.remove(List[2])
data2_list.remove(List[3])
data2_list.remove(List[4])

print("data1에만 있는 단어 개수: ", len(data1_list))
print("========== data1에만 있는 단어 목록 ==========")
print("\n".join(data1_list))
print("-------------------------------------------------")
print("data2에만 있는 단어 개수: ", len(data2_list))
print("========== data2에만 있는 단어 목록 ==========")
print("\n".join(data2_list))
