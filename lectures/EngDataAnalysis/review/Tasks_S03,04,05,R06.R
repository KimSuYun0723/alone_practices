#Task들 모음

#S05-03
# Plot the values of the two variables of the am & pm pitch variation data, and 
  #draw the best-fit regression line.
#What will be the evening pitch of a person whose morning pitch is 128 Hz.
am = c(144, 147, 148, 172, 170, 133, 141, 144, 146, 148, 152, 149, 143, 138, 
       165, 143, 142, 155, 135, 144) 
pm = c(133, 138, 139, 160, 165, 133, 140, 142, 144, 142, 139, 144, 139, 130, 
       164, 140, 128, 129, 133, 144) 
##############################################################################
lm.pm <- lm(pm~am);lm.pm
plot(am,pm, col = "red")
abline(lm.pm)
summary(lm.pm)
new.am <- data.frame(am = 128)
new.pm <- predict(lm.pm, new.am);new.pm
res.pm <- resid(lm.pm)
plot(am, res.pm)
abline(0,0)


#S05-03b
# 
##############################################################################




#S06-01
#Chi-sq Test
#Metaphoric and non-metapgoric uses of "over"
##############################################################################
#INSTALL
install.packages("reshape")
install.packages("vcd")
library(reshape)
library(vcd)

#contingency table
over <- cbind(c(22,4), c(5,12));over
rownames(over) <- c("Metaphoric", "Non-metaphoric")
colnames(over) <- c("Academic", "Conversations")
over

#Visualization
colors <- c("lightblue", "coral")
barplot(over, beside=TRUE,col = colors, main = "over", xlab = "Variety", ylab = "Frequency")
legend("topright", fill = colors, c("metaphoric", "non-metaphoric"))

#Calculate the each proporsions
prop.table(over)
prop.table(over,1)
prop.table(over,2)

#Calculate the effect size
  #Odd
odd_over <- (22/4) / (5/12);odd_over #13.2
#Academic한 상황에서 metaphoric 한 것이 Conversation에서 metaphoric한 것보다 13배이다.

  #phi-coefficience
assocstats(over) #Cramer's V : 0.557 _ strong association

#Perform the x2 test
chisq.test(over)$expected
chisq.test(over)
a <- 1-pchisq(over, df=1) ;a

#Report the result
#H0 rejected
#Variables associated
#over가 metaphoric한지, non-meta 한지는 academic, conversation에 달려있다.


#R06-01
mt <- c("Leaders with White-House aspirations all say they'll support the president for another term") # Note spaces
#Check the word list and find some better ways of word-tokenization.
##############################################################################
wordlist <- strsplit(mt, split=c(" "));wordlist


#R06-01b
  #From the 'ldt' data, try to pick rows with words:
    # starting with the string "in-"a
    # ending with the string "-in"
    # with internal "-in-"
    # starting with "i" or "e"
    # starting with "in" or "ex"
##############################################################################
data <- paste(readtext("C:/Rpractice/data/ldt.csv"));data
grep("^in", data, value=TRUE)
grep("in$", data, value=TRUE)
grep(".in.", data, value=TRUE) #in으로 시작하면서 중간에 in 있는건 어떻게 처리?
grep("^[i|e]", data, value=TRUE)
grep("^(in)|(ex)", data, value = TRUE)


#R06-02
  #Use the built-in variable 'state.name'
  #Print out all the U.S. state names 
    #starting with "New"
    #consisting of multiple words
    #convert all letters of 's' or 'S' into '$'
    #[Difficult] Convert all vowel letters into uppercase.
    #[Difficult] Convert the initial letter of all the 2nd words into lowercase
      #e.g., New York  New york
##############################################################################
state.name
grep("^new", state.name, value=TRUE)
grep(". .", state.name, value=TRUE) #앞에 글자가 있어야 한다. space만 둬도 되긴함
gsub("[Ss]", "$", state.name)

gsub("([aeiou])", "\\u\\1", state.name, perl = TRUE) #perl이라는 언어(정규표현식은 가장 편리하다고 여겨짐)에서 
gsub("(\\s+)(\\w)", "\\L\\1\\2", state.name, perl=TRUE)

#R06-03
  # Read in the text file "moby_sample.txt" available at eclass
  # Create its wordlist and dataframe with three columns "word", "count" and "length", such as:
    #   -----------------------------------
    #   word count length
    # 1 the 10 3
    # 2 i 9 1
    # 3 and 7 3
    # -----------------------------------
  # Functions in packages "readtext" and tokenizers" will be useful.
##############################################################################
data <- paste(readtext("C:/Rpractice/data/moby_sample.txt"));data
wordlist <- tokenize_words(data);wordlist
wt <- table(wordlist);wt
md <- data.frame(word= names(wt), count = as.numeric(wt), length = nchar(names(wt)));md


#R06-04
  #Remove stop words from the word list of moby_sample.txt.
  #Sort the list, without stop words, in descending order by the variable 'count' 
    #and then in descending order by the variable 'length'.
##############################################################################
data <- paste(readtext("C:/Rpractice/data/moby_sample.txt"));data
library(tokenizers)
library(tidytext)
library(dplyr)
wordlist <- tokenize_words(data);wordlist
wt <- table(wordlist);wt
df <- data.frame(word = names(wt), count = as.numeric(wt), length = nchar(names(wt)));df
s_df <- anti_join(df, stop_words, by=c(word="word"));s_df
index <- order(s_df$length, decreasing=TRUE);index
s_df[index,]


#R06-05
  # Read in and analyze mobydick.txt in R and answer the following questions.
  # Make a word list with a frequency counting, such as:
    #   ------------
    #   word count 
    # 1 the   10    
    # 2  a    22
    # --------------
  # Print most frequent words from rank 1 to 100.
  # What are the 10 most frequently used content words?
  # Analyze its frequency distribution by showing
    # descriptive stats with numbers
    # visualize the distributions
  #Make other analyses showing the characteristics of the novel.
##############################################################################
data <- paste(readtext("C:/Rpractice/data/mobydick.txt"));data
library(tokenizers)
wordlist <- tokenize_words(data);wordlist
wt <- table(wordlist);wt
df <- data.frame(word = names(wt), count=as.numeric(wt));df
library(tidytext)
library(dplyr)
df2 <- anti_join(df, stop_words, by=c(word="word"));df2
index <- order(df2$count, decreasing=TRUE);index 
df3 <- df2[index,] #Frequency 기준 내림차순
df3[1:100] #상위 100개개
df3[1:10,] #상위 10개

library(moments)
skewness(df3[1:100,]$count)
hist(df3[1:100,]$count) #이게 맞노........
#Make other analyses showing the characteristics of the novel.\

#R06-06
  #Download ldt data and save it into a data frame.
  #Change the data frame into a tibble.
  #Verify its contents.
  #Print the most frequent word and its frequency.
##############################################################################
data <- read.csv("C:/Rpractice/data/ldt.csv");data
tb <- as_tibble(data);tb
index <- order(tb$Freq, decreasing=TRUE);index
tb[index,][1,]$Word
tb[index,][1,]$Freq

#R06-07
  #Use the ldt data
  #Calculate the square root of the mean frequency of the 20 most frequent words.
  #Use the operator '%>%' of the package 'dplyr'
##############################################################################
data <- read.csv("C:/Rpractice/data/ldt.csv");data
library(dplyr)
index <- order(data$Freq, decreasing = TRUE);index
freq_20 <- data[index, ][1:20,];freq_20
freq_20$Freq %>% mean %>% sqrt

#R06-08
# Compute the logarithm of `x`, return its absolute values, compute the exponential function and round the result to two decimal points.
# x = c(0.109, 0.359, 0.63, 0.996, 0.515, 0.142, 0.017, 0.829, 0.907)
# Use functions round(), exp(), abs(), log()
##############################################################################



#R06-09
  #Analyze President Obama's 2009 speech (obama09.csv) focusing on the words he used most frequently.
  #Compare the result with President Trump's inaugural speech (trump.csv).
##############################################################################









