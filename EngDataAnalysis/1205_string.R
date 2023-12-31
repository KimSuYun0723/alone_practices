#last HW
state.name
grep("^new", state.name, value=TRUE)
grep(". .", state.name, value=TRUE) #앞에 글자가 있어야 한다. space만 둬도 되긴함
gsub("[Ss]", "$", state.name)

gsub("([aeiou])", "\\u\\1", state.name, perl = TRUE) #perl이라는 언어(정규표현식은 가장 편리하다고 여겨짐)에서 
gsub("(\\s+)(\\w)", "\\L\\1\\2", state.name, perl=TRUE)


#
install.packages("readtext")
install.packages("tidyverse")
install.packages("tokenizers")
library(readtext)
library(tidyverse)
library(tokenizers)
md <- paste(readtext("C:/Rpractice/data/mobydick.txt")) # or

mywords <- tokenize_words(md); mywords
class(mywords)

num_w = length(mywords[[1]]); num_w

# sentence tokenization
mysents <- tokenize_sentences(md); mysents #에러뜸. 왜지?
num_s <- length(mysents[[1]])

sorted_w = sort(table(mywords), decreasing=T)
mdf = data.frame(word = names(sorted_w), count = as.numeric(sorted_w), length=nchar(names(sorted_w)))
head(mdf)
mdf$count

#nchar으로 length라는 3번쨰 칼럼 만들어주면 됨

#tokenizers 라는 패키지에 있는 tokenize_words를 쓰고 싶을 땐 지정해야해. 똑같은 이름의 함수가 여러개라서
mywords <- tokenizers::tokenize_words;mywords

install.packages("tidytext"); library(tidytext)
head(stop_words)
class(stop_words)

library(tidytext)
library(dplyr)
mdf2 <- anti_join(md, stop_words, by=c(word="word"))

##########
md <- paste(readtext())
words <- tokenize_words(md)
moby = data.frame(word ~names(freq), count = as.numeric(freq), length=nchar())
moby_mod = anti_join(moby, stop_words, by = c(word = "word"))
moby_
mdf2[order(-mdf2$count, -mdf2$length),]

install.packages("readr", dependencies = TRUE)
install.packages("wordcloud2", dependencies = TRUE)
install.packages("viridis", dependencies = TRUE)

library(tidytext)
library(readr)
library(ggplot2)
library(wordcloud2)
library(dplyr)
library(tidyverse)
library(viridis)

trump <- read_csv("C:/Rpractice/data/trump.csv")
trump <- read.csv(file.choose())
#Word Frequency Counting
trump <- trump %>% unnest_tokens(word, text)
trump <- data.frame(trump) # to a more familiar data structure
trump <- trump %>% count(word, sort =TRUE)
trump <- trump %>% anti_join(stop_words) # removing stop words


df.trump <- trump[trump$n > 2,] # leaving words over 3 characters
ggplot(df.trump, aes(x=reorder(word,n), y=n)) + geom_col() + coord_flip() + ggtitle("Trump's 2013 Speech Most Used Words")
wordcloud2(data=trump)

#Obama
library(tidytext)
library(readr)
library(ggplot2)
library(wordcloud2)
library(dplyr)
library(tidyverse)
library(viridis)

obama <- read_csv("C:/Rpractice/data/trump.csv")
obama <- read.csv(file.choose());obama 

#Word Frequency Counting
trump <- trump %>% unnest_tokens(word, text)
trump <- data.frame(trump) # to a more familiar data structure
trump <- trump %>% count(word, sort =TRUE)
trump <- trump %>% anti_join(stop_words) # removing stop words


df.trump <- trump[trump$n > 2,] # leaving words over 3 characters
ggplot(df.trump, aes(x=reorder(word,n), y=n)) + geom_col() + coord_flip() + ggtitle("Trump's 2013 Speech Most Used Words")
wordcloud2(data=trump)


