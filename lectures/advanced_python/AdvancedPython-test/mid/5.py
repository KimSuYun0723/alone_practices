print("==========5번 문제==========")

data1 = ['the', 'stunning', 'canvas', 'of', 'the', 'twilight', 'sky', 'was', 'adorned', 'with', 'the', 'radiant', 'hues', 'of', 'the', 'descending', 'sun']
data2 = ['the', 'resplendent', 'colors', 'of', 'the', 'setting', 'sun', 'adorned', 'the', 'twilight', 'sky', 'like', 'a', 'beautiful', 'painting']

data3 = data1[:] #data3 새로운 리스트
data3.extend(data2)

print(sorted(list(set(data3))))