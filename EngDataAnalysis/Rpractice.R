version
date()
help(version) # or ?version
getwd()
8*3+4
print ("Hello R")
35/4; print("Multiple commands")

a <- 3
b <- 8
c <- a+b

print(a)
a

#나머지, 몫 활용하기
t <- 2237
hour <- t %/% 60
min <- t %% 60
cat (t, "minutes equals to", hour, "hours", min, "minutes")

#대문자, 소문자로 바꾸기기
hi <- "hello, seoul"
okay <- "OKAY, KOREA"
toupper(hi)
tolower(okay)

#숫자와 캐릭터는 정렬이 다름름
m<- c("-1", "8", "-3", "6", "0")
n <- c(-1, 8,-3, 6, 0)
sort(m)
sort(n)

#function making
say.hello <- function(x){
  cat ("Hello, HUFS", x)
}
say.hello(3) 
#argument있는데 그냥 실행하면 에러남

say.hello <- function(x="Jane"){
  cat ("Hello, HUFS", x)
} #여기서 argument는 default라서 없이 실행해도 에러 안남
say.hello(3) 
