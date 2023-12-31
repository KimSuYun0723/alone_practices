#R06_text_analysis_base

#텍스트에서 가장 짧은 & 긴 단어를 찾을 때
data1 = "Leaders with White-House aspirations all say they'll support the president for another term"
mt = c(data1)

    #1
wordlist <- strsplit(mt, split= c(" "));wordlist #strsplit는 class가 lsit
#wordlist <- strsplit(mt, split=c(" |-"));wordlist 
mw <- unlist(wordlist);mw #unlist는 class가 character
index <- which(nchar(mw)==max(nchar(mw))) #nchar 쓰려면 character로 바꿔야지지
mw[index]
nchar(mw[index])

  #2
library(tokenizers)
wordlist <- tokenize_words(mt)
mw <- unlist(wordlist)
mw2 <- unlist(wordlist)
md <- data.frame(Word = mw2, Length = nchar(mw2));md
index2 <- which(md$Length==max(md$Length))
md$Word[index2]
md$Length[index2]



#Tidy text data format



#유용한 함수들
  #nchar() --> \n포함해서 계산함.
  #strsplit() & unlist(new)
  #paste()
a <- "hello"
b <- "Seoul"
paste(c(a,b)) #"hello" "Seoul"
paste(a,b) #"hello Seoul"
paste(a,b, collapse ="") #"hello Seoul"
paste(c(a,b), collapse="") #"helloSeoul"
  #strwrap()
mt <- "Call me Ishmael. Some years ago--never mind how long 
precisely--having little or no money in my purse, and 
nothing particular to interest me on shore, I thought I would 
sail about a little and see the watery part of the world. It 
is a way I have of driving off the spleen and regulating the 
circulation. " #\n 포함함
clean.mt <- strwrap(mt, width = 60, indent = 3) #\n 기준으로 character 여러개
writeLines(clean.mt) #\n기준 라인 1개씩씩
  #grep()
month.name
grep("a", month.name)
grep("a", month.name, value = TRUE)
grep("^[A|J]", month.name, value = TRUE) #첫글짜가 A혹은 J
grep("[y|t]$", month.name, value = TRUE) # 마지막 글자
  #grepl()
grepl("ber", month.name) # logical vector(T/F)가 12개 나옴
  #sub()
sub("ber", "BER", month.name) # substitution
sub(".*r", "", month.name) # regular expression
  #gsub() --> 모든걸 다 바꿈
gsub("a", "A", "January") # global application
  #sprintf()
n <- 4
sprintf("The number is: %04d", n) #%0xd --> 앞에 0몇개 붙일지 정수
n <- 0.666666666666666
sprintf("The number is: %.2f", n) #%0xd --> 앞에 0몇개 붙일지 정수



library(readtext)
#reading in text files --> k <- paste(readtext())
md = paste(readtext("C:/Rpractice/data/moby_sample.txt")) # or
DATADIR <- "PATH"
md = readtext(paste0(DATADIR, "*.txt"))

md = readtext(paste0(DATADIR, "*.doc"))
Encoding(md$text)



library(tidyverse) #tibble, readr, dplyr, magrittr, ggplot2



library(tokenizers) #tokenize_words(), tokenize_sentences()]
mywords <- tokenize_words(md);mywords
sorted_w <- sort(table(mywords));sorted_w
mdf <-data.frame(word = names(sorted_w), count = as.numeric(sorted_w));mdf

mdf$count



#stop words
library(tidytext)
library(dplyr)
head(stop_words)
stop_words
anti_join(mdf, stop_words, by=c(word="word"))



#tibbles  --> 각 row, column 넘버 제공 / 컬럼의 데이터타입 제공, 10줄만 프린트
df
tb <- as_tibble(df);tb


#useful 'dplyr' functions
ldt <- read.csv("C:/Rpractice/data/ldt.csv");ldt
head(ldt)
dplyr::filter(ldt, Length>10) # Just as: subset(ldt, Length >10)
dplyr::select(ldt, Word, Freq) # Just as: subset(ldt, select=c(Word, Freq))
arrange (ldt, Word) # ascending  # just as : ldt[order(ldt$Length),]
arrange (ldt, desc(Word)) # descending # just as: ldt[order(-ldt$Length),]
arrange (ldt, Word, Length) # two criteria

#ggplot2
library(ggplot2)
ggplot(ldt, aes(x=Length, y=Mean_RT)) + geom_point()
ggplot(ldt, aes(x=Length, y=Mean_RT), label = Word) + geom_point() #왜 라벨 word로 안뜨노..



