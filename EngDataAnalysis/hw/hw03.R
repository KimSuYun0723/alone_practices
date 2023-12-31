#R01-27
chart <- data.frame(
  Name = c("John", "Tammy", "Tim", "Jerry", "Carl", "Michael"),
  Age = c(35, 26, 48, 22, 39, 28),
  Position = c("Researcher", "Dealer", "CEO", "Sales", "Manager", "Sales"),
  Degree = c("Phd", "BA", "MBA", "BA", "MA", "BA"),
  Income = c(165000, 46000, 145000, 39000, 82000, 44000),
  Weight = c(182, 156, 188, 142, 152, 137),
  IQ = c(128, 101, 131, 133, 126, 122)
)

#a. Display the data after removing columns "Age", Degree" and "IQ". 
data <- subset(chart, select = -c(Age, Degree, IQ))
data 

  #prof
data$Age <- NULL; data
data$Degree <- NULL; data
data$IQ <- NULL; data
#OR my method.


#b. Calculate average IQ of the people over 30.
num <- order(chart$Age > 30)
num <- which(chart$Age > 30) # 이렇게 해야지지
iq <- mean(chart$IQ[num])
cat("Average IQ of the people over 30 is", iq)

  #prof
mean(subset(chart, Age >30)$IQ)

md2 <- subset(chart, Age>30)
sqrt(round(meadn(md2$IQ),2))

library(dplyr)
md2$IQ %>% mean %>% round(2) %>% sqrt %>% round(2) #dplyr 패키지지에 이런 hyper-operator가 있음. 

md[md$Age >30, ]$IQ %>% mean #martix를 사용하는 방법도 있겠지, subset도 있고. 자기가 편리한대로 사용


#c. Display the name and age of the individual with the lowest income among those who do not hold a 'Sales' position.
chart2 <- subset(chart, Position != "Sales") #No "Sales"
where <- which.min(chart2$Income)
info <- chart2[where,]
answer <- subset(info, select = c(Name, Age))
answer

  #prof
ns <- subset(md, Position != "Sales")
ind <- order(ns$Income); ind # ascending 일테니까,
ns$Name[ind][1] #1로 뽑으면 되겠지. 
ns$Age[ind][1]

ind2 <- which(ns$Income == min(ns$Income))
ns$Name[ind2]; ns$Age[ind2]


#d. Compare the income of individuals with an IQ score exceeding or equal to 130 to those with IQ scores below 130
compare1 <- subset(chart, IQ>=130)
compare2 <- subset(chart, IQ<130)

  #1. Compare with calculating average
over130 <- mean(compare1$Income)
less130 <- mean(compare2$Income)
if (over130 > less130){
  print("The income of individuals whose IQ score is exceeding or equal to 130 paid more than those with IQ scores below 130")
} else if (over130 > less130){
  print(print("The income of individuals whose IQ score is exceeding or equal to 130 paid less than those with IQ scores below 130"))
} else if (over130 == less130) {
  print("Their averages are same!")
}

  #2. calculating middle value
ov130 <- median(compare1$Income)
le130 <- median(compare2$Income)

if (ov130 > le130){
  print("The median income of individuals whose IQ score is exceeding or equal to 130 paid more than those with IQ scores below 130")
} else if (ov130 > le130){
  print(print("The median income of individuals whose IQ score is exceeding or equal to 130 paid less than those with IQ scores below 130"))
} else if (ov130 == le130) {
  print("Their averages are same!")
}


  #prof
iq_over <- md[md$IQ >= 130, ]; iq_over
iq_under <- md[md$IQ < 130, ] ; iq_under
iq_over$IQ %>% mean
iq_under$IQ %>% mean



#R01-28
library(languageR)
head(verbs)
verbs[order(verbs$Verb, -verbs$LengthOfTheme), ]

  #prof
library(languageR)
verbs

md <- verbs[order(verbs$Verb), -verbs$LengthOFTheme] #descending order
md %>% head




##++
md <- data.frame(
  Name = c("John", "Tammy", "Tim", "Jerry", "Carl", "Michael"),
  Age = c(35, 26, 48, 22, 39, 28),
  Position = c("Researcher", "Dealer", "CEO", "Sales", "Manager", "Sales"),
  Degree = c("Phd", "BA", "MBA", "BA", "MA", "BA"),
  Income = c(165000, 46000, 145000, 39000, 82000, 39000), #39000 2명명
  Weight = c(182, 156, 188, 142, 152, 137),
  IQ = c(128, 101, 131, 133, 126, 122)
) ; md

index <- which.min(md$Income) #min은 동점일 때 1번쨰 인덱스만 가져옴.
md$Name[index] 

#and
ind2 <- which(md$Income == min(md$Income)) #처럼 해야 possible to solve

