# "sen_list.txt"에 저장
with open("sen_list.txt", "w") as file:
    # emily.txt 파일 열고 읽기
    with open("emily.txt", "r") as ffile:
        text = ffile.read()
        #문장 쪼개기
        sentences = text.split(". ")
        List = []
        for i, sentence in enumerate(sentences):
            List.append(f"Line {i+1}: {sentence}")
        String = "\n".join(List)
        file.write(String)