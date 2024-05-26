mt <- c("Leaders with White-House aspirations all say they'll support 
        the president for another term")

#[Method 1]
wordlist <- strsplit(mt, split=c(" ")) # split the string into words
wordlist #space가 있어서 막 아무거나 갖고 온거야
class(wordlist) #list : 쓰기 불편

# wordlist <- strsplit(mt, split=c(" |-")) # separate 'white' and 'house'
mw <- unlist(wordlist) # list-> vector

index <- which(nchar(mw) == max(nchar(mw))) # Note which.max() doesn't work
mw[index]
nchar(mw[index])

#R06-01
mt <- c("Leaders with White-House aspirations all say they'll support the president for another term") # Note spaces
wordlist <- strsplit(mt, split=c(" "));wordlist

#method 2
install.packages("tokenizers")
library(tokenizers)
wordlist <- tokenize_words(mt) #tokenize words function??? 을 쓴다~ 하고 넘어가도 될 것 같다.
mw <- unlist(wordlist) # from the 'list' to a 'vector' with words
mw2 <- unlist(wordlist); mw2 # from the 'list' to a 'vector' with words
md <- data.frame(Word = mw2, Length = nchar(mw2)); md
index2 <- which(md$Length == max(md$Length))
md$Word[index2]
md$Length[index2]

mt <- "Call me Ishmael. Some years ago--never mind how long 
precisely--having little or no money in my purse, and 
nothing particular to interest me on shore, I thought I would 
sail about a little and see the watery part of the world. It 
is a way I have of driving off the spleen and regulating the 
circulation. "
clean.mt <- strwrap(mt, width = 60, indent = 3)
writeLines(clean.mt)

month.name
grep("a", month.name) # index only
grep("a", month.name, value = TRUE) # note "April", "August"
grep("A", month.name, value = TRUE) 
grep("ber", month.name, value = TRUE)
grep("^[A|J]", month.name, value = TRUE) # initial
grep("[y|t]$", month.name, value = TRUE) # final
grepl("ber", month.name) # logical vector

# Substitution
sub("ber", "BER", month.name) # substitution
sub(".*r", "", month.name) # regular expression
gsub("a", "A", "January") # global application: 여러번 나오면 싹 다 바꿔달라!
#* :zero or more

subset(ldt, grepl("in", ldt$Word))
# Or, 
ldt[grepl("in", ldt$Word), ] 

#R06-01b
#in~
subset(ldt$Word, grepl("^in", ldt$Word))
#~in
subset(ldt$Word, grepl("in$", ldt$Word))
#-in-
subset(ldt$Word, grepl(".in.", ldt$Word))
#statring with i or e
subset(ldt$Word, grepl("^[i|e]", ldt$Word))
#starting with in or ex
subset(ldt$Word, grepl("^(in|ex)", ldt$Word))
#{} : character로 접근. 한 글자씩 중에 1개. 선택되는..
#[] 안에 있는것 중에 하나, 고를거 아니면 ()