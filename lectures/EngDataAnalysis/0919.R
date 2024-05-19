#0919
(.packages)
(.packages(all.available=TRUE))

#R.profile
Sys.getenv("HOME")

install.packages("languageR") #설치시에는 quotation mark #dslabs라는 함수도있음
library(languageR) #불러올 때는 없어도됨
ls("package:languageR") #objects list
lsf.str("package:languageR") #function, arguments도 다 보여줌줌
verbs
head(verbs)
tail(verbs, 10) #10 없으면 디폴트로 보여주겠지
colnames(verbs)

install.packages("dslabs")
library(dslabs)
head(murders)
summary(murders)
str(murders)

x <-2388
y<- c("a", "b")
class(3+4i)
typeof(x)
typeof("x")
length("x") #1
length(y)
is.character(y) #quote를 주면 다 character, 만약 numeric이면 FALSE
is.character(x)

z <- c(1:100000)
class(z)
k <- as.double(z)
class(k)
p <- as.character(z)
class(p)

object.size(z) #4MB
object.size(k) #8MB
object.size(p) #64MB

x <- c(3.5, -4.8, 5.1)
class(x)
y<-as.integer(x) #아예 버림해버리는, information loss가 생김.
class(y)
y 

x <- c("3.5", 6, 5.1, "HUFS", TRUE)
class(x)
x

tmp <- c("4.8") #;;;;

capital <- c("Seoul", "Washington", "Tokyo", "Beijing", "London")
country <- c("Korea", "USA", "Japan", "China", "UK")
names(capital) <-country
capital
capital["USA"]

capital <- c("Korea"="Seoul","USA"="Washington", "Japan"="Tokyo", "China"="Beijing", "UK"="London")
a <- capital["USA"]
print(a)

library(dslabs)
head(murders)
murders$state
murders$population
mean(murders$population)
subset(murders, select =c("state", "population"))
#Select specific rows
subset(murders, population<1000000)

#Write a code that prints out states with more than 500 murder cases in 2010
x<-subset(murders, total>500) #select 하거나 variable에 저장한 뒤에 $
x$state

#R01-20
nums <- c(20:1)
nums[3:6]
nums[3,6]
nums[c(3,6)]
nums[18:20] #20개니까 이렇게 하는거지, 몇개이든지 뽑아낼 수 있는걸 생각해
n_item <- length(nums)
nums[(n_item-2):(n_item)]# 괄호 안쓰면 안되나봐
nums[-1:-5]

nums[n_item- 2:n_item] # 17 18 19 20, priority 문제임.
nums[20-2:20] #nums[20-(2:20)] sequence니까 2,3,4, 하나씩 넣어서 뺴면~



head(murders)

index <- murders$population > 10000000
index
index <- which(murders$population>10000000)
index

murders$state[index]

#R01-21_p20
head(murders)
index <- which(murders$region =="West")
index
murders$state[index]
subset(murders, region=="West") #select는 column을 볼떄 하는 것


install.packages("dslabs", dependency=TRUE)
library(dslabs)
help(package="dslabs")
head(murders); colnames(murders)
murders$state
subset(murders, select=c("state", "population"))
subset(murders, population < 1000000)



###########################################################3
#individual practice

#R01-19
subset(murders, total>500)

nums <- c(20:1)
logi <- nums < 10
nums[logi]

#R01-20
#a
nums[3:6]
nums[3,6] #Error in nums[3, 6] : incorrect number of dimensions
nums[c(3,6)]

#which() _index만 반환환
which.max(nums)
which.min(nums)
nums
md <- c("Seoul", "New York", "Paris", "Tokyo")
which(md == "Paris")
md2 <- c(25,37,33,2,21)
which.max(md2)

index <- murders$population > 10000000
index
index <- which(murders$population > 10000000)
index
murders$state[index]

#R01-21_ from murders' data
#a. Using 'vector indexing', write a code that prints out states in the West region
  #my version
index <- murders$region == "West"
murders$state[index]

  #professor's
head(murders)
index <- which(murders$region =="West")
index
murders$state[index]
subset(murders, region=="West") #select는 column을 볼떄 하는 것

#b.Using 'subset()', print out all columns of 'West' States
columns <- names(murders)
columns
subset(murders, murders$region =="West") #subset should be logical
subset(murders, murders$state[index]) #Error-> subset should be logical



