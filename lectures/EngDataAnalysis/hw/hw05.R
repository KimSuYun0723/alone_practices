# S01-03
#table(), names() may be helpful.

mymode <- function(v) {
  #vector인지 검증할수도 있겠지만 일단은 하지말자
  data <- table(v) ; data
  ind <- max(data) ; ind
  answer <-  names(data[data == ind]) ; answer
  cat(answer)
}

#professor
mycode <- function(x) {
  t<- table(x)
  ind <- which(t == max(t))
  names(ind)
}

var = c(2, 3, 5, 5, 6, 7, 7, 8, 10)
cities = c("Paris", "Munich", "Seoul", "Bankok", "Seoul", "Tokyo", "Incheon", "Beijing", "Paris", "London", "London")
ldt = read.csv(file.choose())

mymode(var)
mymode(cities)
mymode(ldt$Length)


# S01-05
freq <- ldt$Freq
#Descriptive statistics of the data (range, central tendency, dispersion)
  #Range
ran <- range(freq); ran #range
max <- max(freq); max #max
min <- min(freq); min #min

  #Central tendency
av <- mean(freq); av #mean
m <- median(freq); m #median
fr_word <- ldt$Word[which(freq == max(freq))]; fr_word #mode of "words"
data <- table(freq)
fr_fr <- names(data[data==max(data)]) ;fr_fr #mode of "frequency"

  #Dispersion 
var(freq) #varience
sd(freq) #standard deviation 1
sqrt(var(freq)) #standard deviation 2
IQR(freq) #Interquartile range


#Visualization of data distributions
  #histogram
hist(freq, main="Frequency", ylab = "freqency", col = "pink")  #the 같은게 너무 많을거라, 사실 다 제거해야하지만 지금은그냥.
  #boxplot
boxplot(freq, main="Frequency", ylab = "freqency", col = "purple")



#Display of a list of 10 most frequent words.
c <- order(ldt$Freq, decreasing = TRUE)[1:10]
num =1
for (i in c) {
  cat(num, ")", ldt$Word[i], ":", ldt$Freq[i], "\n")
  num = num+1
}

#professor
w <- ldt$word[order(ldt$Freq, decreasing = TRUE)] [1:10]
w <- ldt$word[order(ldt$Freq, decreasing = TRUE)] %>% head(10)
w[1:10]



