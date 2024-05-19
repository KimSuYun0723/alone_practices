#22
phone_code <- function(country){
  countries <- c("Korea", "UK", "USA", "Japan", "China", "Russia", "Vietnam")
  phones <- c(82, 44, 1, 81, 86, 7, 84)
  names(phones) <- countries
  country <- as.character(country)
  
  #To print only 82
  code <- phones[country]
  print(as.numeric(code))
}
phone_code("Korea")
#substitute(), deparse() 사용하면 ""없어도 가능은 함


#professor
phone_code2 <- function(c){
  countries <- c("Korea", "UK", "USA", "Japan", "China", "Russia", "Vietnam")
  code <- c(82, 44, 1, 81, 86, 7, 84)
  names(code) <- countries
  cat(code[c])
}
phone_code2("Korea")


#23
#speed.R 파일을 만들어야 하나, hw02 파일에 한꺼번에 담아야 하므로 대신 함수명을 speed로 설정
speed <- function(){
  name <- c("John", "Lisa", "Sue", "Tony")
  distance <- c(1.3, 4.96, 4.46, 6.4)
  time <- c(11, 30, 38, 47)
  hour <- time/60
  index <- 1:length(name)
  
  speed <- distance[index]/hour[index]
  names(name) <- speed
  where <- which.min(speed)
  cat("The runner who has the fastest speed is", as.character(name[where]))
}
speed()


#professor
fastest_runner <- function(){
  name <- c("John", "Lisa", "Sue", "Tony")
  distance <- c(1.3, 4.96, 4.46, 6.4)
  time <- c(11, 30, 38, 47) #시속으로 바꿔서 하는 방법
  speed <- distance / time
  cat(name[which.max(speed)]) #max로 해야지 진짜 븅신이니
  cat(speed)
}

fastest_runner()


#24
#danger.R 파일을 만들어야 하나, hw02 파일에 한꺼번에 담아야 하므로 대신신 함수명을 speed로 설정
danger <- function() {
  install.packages("dslabs")
  library(dslabs)
  news <- subset(murders, select=c("state", "population", "total"))
  
  tot <- news$total
  popul <- news$population
  ratios <- (tot/popul)*100
  
  num1 <- order(ratios, decreasing=TRUE)
  news$ratio <- ratios
  
  answer1 <- subset(news, ratio > ratios[num1][11])
  num2 <- order(answer1$ratio, decreasing=TRUE)
  answer0 <- answer1$state[num2]
  print(answer0)
}
danger()


#professor
library(dslabs)
ratio <- murders$population / murders$total
ratio
index <- order(ratio); index

head(murders$state[index], 10)
