#preparation for the quiz on 20231017

#R01-basics

#Vocabs
#1. Functions : a set of statements that perform a task
#2. Operators : an object that tells the interpreter(or compiler) to perform a specific task
#3.package : a collection of useful functions and data for specific tasks

#variables
#.2name <- 1; .2name
#na-me <- 1;na-me
#^name<- 1;^name
#6thnam<- 1;6thnam
#name% <- 1;name%
#_name <- 1; _name


#available variables
name.name <- 1;name.name
._name <- 1;._name
NamE <- 0; Name


#Checking variables
ls()


#Deleting variables
rm(._name)
ls()

#Types of func --> sqrt // c, sum, sort, mean, max, help, tolower, toupper, nchar, abs, round
help(sqrt)
help(seq)

#checking function's arguments 
args(sqrt(5))
hi.person <- function(first, last){
  print (sprintf("Hi %s %s", first, last)) 
}

hi.person <- function(first = "Bill" , last = "Gates"){
  print (sprintf("Hi %s %s", first, last))
}
hi.person("Steve")


#data types --> atomic vector, vector, list, factor, matrix, df

#Examine data types
class()
typeof()
mode()
is()

# check data attributes
str()
length()

#Test types
is.numeric() #...

#make a conversion to a specific type
as.numeric()
as.integer()
as.character()
as.double()

yvector <- c(23, "Hello", -3.42)
yvector

nums <- c(1,2,3,4,5,6,7,9,8)
logi <- nums <9; logi
order(logi)
nums[order(logi)]

#plotting in R - package : ggplot2
install.packages("ggplot2")
library(ggplot2)

#basic scatter plot
library(dslabs)
murders$rate <- murders$total / murders$population*10^5
plot(murders$rate, murders$total, col="red")
#arguments가 있음 --> main = "my graph", col="red"

#basic histogram
hist(murders$rate, main = "Murder cases")
boxplot(rate~region, data = murders, col=c("red", "blue"))

#two plots on one plane
par(mfrow=c(1,2))
boxplot(rate~region, data = murders)
hist(murders$rate)
par(mfrow=c(1,1))
hist(murders$population)

ggplot(data=murders)+geom_histogram(aes(x=population))


par(mfrow=c(2,2))
for (i in 1:4) {
  hist(rnorm(500), main = "hihi")
  main=paste("Trial", i, sep =" ")
}
par(mfrow=c(1,1))
##########################################################################
#Codes


#R01-07
a <- (1:4); a
b <- a*3; b

#R01-09
cha <- "hello, seoul"
up<- toupper(cha); up
ok <- "OKAY, KOREA"
do <- tolower(ok);do

m <- c("-1", "8", "-3", "6", "0")
a <- sort(as.numeric(m), decreasing = TRUE); a

sqrt(25)
log(8)
log(8, base=2)
log(8, base=exp(1))
log(8, 10)
log(8,3,10)
log(8, x=3, base=10)

#R01-12
qe_solution <- function(a,b,c) {
  x1 <- (sqrt(b**2-4*a*c)-b)/2*a
  x2 <- (sqrt(b**2-4*a*c)+b)/2*a
  cat(x1, "or", x2)
}
qe_solution(5,6,1)

######################################################################
#R02_packages

#packages install
install.packages("packagename", dependencies = TRUE)
install.packages("name", respos="http://R-Forge.R-project.org") #if you want to access a specific repository

#Updating
update.packages()

#Uninstallation
remove.packages("packagename")


#Check installed packages-------------------------다시 search 해보기
(.packages()) #current package
gerOption("defaultPackages") #default packages
(.packages(all.available = TRUE))
library # all packages and summary of each

#Using packages
library("packagename")

Sys.gentv("HOME") #Your default home directory
ls("package:pkgname") # Check what functions and df are available from that package
lsf.str("package:pkgname") #in detail

#functions --> head, tail, colnames, summary, str
#packages --> dslabs, languageR, 

people <- c("Lee", "Kim", "Song", "Park")
score<- c(23,15,11,68)

md <- data.frame(people, score)
md[,1]















