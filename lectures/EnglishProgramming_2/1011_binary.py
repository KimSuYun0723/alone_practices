#Binary Data
with open("Aesop_001_Task2_009.TextGrid.utf16", "r", encoding = "utf-16") as f:
    text = f.read()
    print(text)

import struct
packed = struct.pack('f', 123.456)
unpacked = struct.unpack('f', packed)
print(unpacked[0])

import struct
packed = struct.pack('12s', '대한민국'.encode())
print(packed) #인코드를 한걸 보고 싶을 수도 있잖아.
unpacked = struct.unpack('12s', packed)
print(unpacked[0].decode()) #문자열일때만 encode했다가 decode하는 과정이 필요함. 아니면 우리가 못알아 먹으니까
#그리고 unpack이 튜플이라, 0번 인덱스로 하면됨. 튜플은 인코드 디코드를 못해

import struct
city_info = [
# CITY, Latitude, Longitude, Population
('서울'.encode(encoding='utf-8'), 37.566535, 126.977969, 9820000),
('뉴욕'.encode(encoding='utf-8'), 40.712784, -74.005941, 8400000),
('파리'.encode(encoding='utf-8'), 48.856614, 2.352222, 2210000),
('런던'.encode(encoding='utf-8'), 51.507351, -0.127758, 8300000)
]
struct_fmt = '=16s2fi' # char[16], float[2], int
with open('cities.dat', 'wb') as file:
    for city in city_info:
        file.write(struct.pack(struct_fmt, *city)) # * 연산자가 튜플이나 리스트의 요소를 하나씩 분리해서 매개변수로 입력해줌

#인코드 디코드 둘다 있는
import struct

struct_fmt = '=16s2fi' # char[16], float[2], int
struct_len = struct.calcsize(struct_fmt) #calcsize 데이터의 크기를 확인할 수 있는 함수
cities = []

with open('cities.dat', "rb") as file: #바이너리라서 rb
    while True:
        buffer = file.read(struct_len) #사이즈를 주고 읽기_바이너리파일이니까
        if not buffer: break #내용이 없으면 읽지 않음 -> 파일의 끝에 도달하면 while에서 나옴
        city = struct.unpack(struct_fmt, buffer) #buffer(내용)를 포맷에 맞게 unpack하고
        cities.append(city) #리스트에 담기

    for city in cities:
        name = city[0].decode(encoding='utf-8').replace('\x00', '') #pack() 하는 과정에서 문자를 할당하고 남은 공간에 채워진\x00를 디코딩한 후 빈 문자열로 다시 바꿔 넣음
        print('City:{0}, Lat/Long:{1}/{2}, Population:{3}'.format(name, city[1], city[2], city[3]))


