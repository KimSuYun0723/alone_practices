data1 = "Once upon a time, there was a young man named Jack who lived in a small village."

data = data1.replace(",", " ,").replace(".", " .")
data = data.split(" ")
print(data)