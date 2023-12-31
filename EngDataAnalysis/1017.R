ldt <- read.csv(file.choose()) #ldt data : frequency가 반응시간에 영향을 미칠 것이다~
ldt <- read.csv("C:/Rpractice/data") #WHY???
ldt

library(dplyr)

head(ldt)
str(ldt)

md <- ldt$length
md2<- ldt$Mean_RT
hist(md2, main= "My graph", col="yellow")


mymedian <- function(x) {
  x <- sort(x)
  
  if (length(x)%%2 ==0) {
    ind1 <- (length(x)%/%2)
    ind2 <- (length(x)%/%2)+1
    return((ind1+ind2)/2)
  } else {
    ind <- (length(x)+1)%/%2
    return(x[ind])
  }
}

a<- c(2,4,4,5,8,9)
b<- c(2,4,5,8,9)

median(a)


#rnorm (x, mean, sd)

md <- rnorm(10000, 175, 5)
hist(md, breaks=20, prob=T) #try with 

lines(density(md)) # or
plot(function(md)dnorm(md, mean=175, sd=5), 160, 190, add=TRUE) 

              