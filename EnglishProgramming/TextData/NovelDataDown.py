import nltk
nltk.download('gutenberg')
df = nltk.corpus.gutenberg.raw('austen-emma.txt')
print(df)
f = open("austen-emma.txt", "w")
f.write(df)
f.close