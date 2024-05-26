md <- rnorm(10000, 175, 5)
hist(md, breaks=20, prob=T) #try with 
lines(density(md)) # o

x<- dnorm(md, mean=165, sd=5)
y<- dnorm(md, mean=185, sd=5)
#probability 계산은 더 힘듬. : 그 면적을 계산(적분)해야하기 때문, 
#likely --> 간단하게 classify할 수 있음._dnorm의 역할

#S02-04
md <- rnorm(5400, 4.5, 1.4)
hist(md, breaks = 20, prob =T); lines(density(md)) #3.7%정도이다다
1-pnorm(7,4.5,1.4, lower.tail = FALSE)

5400 * pnorm(5,4.5,1.4) - pnorm(4,4.5,1.4) #1506~7명 정도!

rnorm(254, mean = 3.29, sd = 0.73)

library(moments)
kurtosis(md)

ldt$Freq %>% hist(breaks = 30) #breaks는 data front를 많이 쪼갠단 뜻입니다.


a <- c(0, 21, 22, 40, 42, 47, 48, 48, 59, 61, 67, 68, 72, 80, 80, 83, 87, 88, 89, 93, 97, 98, 100, 100, 100) 
b <- c(0, 0, 0, 0, 0, 0, 4, 8, 17, 22, 28, 38, 42, 44, 46, 58, 62, 62, 66, 67, 67, 72, 73, 73, 88, 88, 89, 100)
c <- c(10, 12, 18, 25, 33, 33, 34, 58, 62, 64, 66, 67, 67, 75, 78, 78, 79, 83, 86, 88, 89, 91, 91, 94)

zscore <- function(x, data){
  z.x <- (x-mean(data))/sd(data)
  return (z,x) #변수에 받으려고 하는거니까 return
}
z_john <- zscore(87, a);z_john
z_lisa <- zscore(67, b);z_lisa
z_kevin <- zscore(75, c);z_kevin

log(ldt$Freq %>% hist) #ND의 그래프가 만들어짐
log(ldt$Freq) %>% skewness #에러남 -> 와이? --> Freq에 0 때문. Freq에 0이 있으면  log계산이 안된다고

log1p(ldt$Freq) #이렇게 해야 에러가 사라짐
log1p(ldt$Freq) %>% skewness



