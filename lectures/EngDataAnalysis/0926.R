#list
num <- c(1, 2, 3, 4)
boo <- c(TRUE, FALSE, TRUE, TRUE, FALSE)
func <- c(mean, sum) # even functions
mylist <- list(num, boo, func)
class (mylist)
print (mylist)
mylist[[2]] # [1] TRUE FALSE TRUE TRUE FALSE, 가장 상위의 아이템을 [[]]처럼 표기기
mylist[[2]][4] # TRUE, 2번째 아이템의 4번쨰 아이템


#factor -> character이기 때문에 필요한 것.
level <- c("good", "okay", "bad", "good", "okay") # variable level has its string values: "good", "bad" and "okay"
level # as string with quotes

level <- factor(level) # recoding into factor
level # as integer factor without quotes
summary(level)
mode(level)

sample(month.name, 2) #month name 중 2개만 뽑아달라

x= sample(month.name, 100000, replace=TRUE) #replace : 1번 뽑았던 것을 다시 뽑아도 괜찮다.
head(x)

object.size(x)
object.size(factor(x)) #byte가 절반으로 감소, efficient하다


#factor: ordered-> factor에 order을 부여할 수 있다다
gem <- c("platinum", "silver", "diamond", "gold")
class(gem)

gem <- ordered(gem)
class(gem)

gem <- factor(gem, levels(gem)[c(4,2,3,1)]) #level redefind
gem

summary(gem); class(gem); typeof(gem)

  #or more explicitly
gem <- factor(gem, levels=c("silver", "gold", "platinum", "diamond"), ordered=TRUE)
gem

#matrix
m<- matrix( 
  c(6, 3, 8, 5, 0, 9), # the data elements
  nrow=3, # number of rows
  ncol=2, # number of columns
  byrow = TRUE) # fill matrix by rows (compare)
m # printing the matrix

m[3, 2] # printing element at 3rd row, 2nd column
m[, 2] # printing the 2nd column elements
m[1, ] # printing the 1st row

  #naming rows and columns of a matrix
dimnames(m) = list(
  c("r1", "r2", "r3"), # row names
  c("c1", "c2")) # column names
  #local processing
m

mean(m[, 2]) # access by column number
mean(m[, "c2"])



#R01-25
phy <- matrix(
  c(18, 170, 62, 20, 182, 68, 36, 178, 79, 44, 165, 63),
  nrow = 4, 
  ncol = 3, 
  byrow = TRUE
)


#df(29p)
phy_matrix <- matrix ( 
  c(18, 20, 36, 44, 
    "m", "f", "m", "f",
    FALSE, FALSE, TRUE, TRUE),
  nrow=4, ncol=3, byrow=TRUE
) ; phy_matrix


name=c("kim", "lee", "lim", "jo")
age=c(18, 20, 36, 44)
sex=c("m", "f", "m", "f")
married=c(FALSE, FALSE, TRUE, TRUE)
phy_list <- list(name, age, sex, married); phy_list


phy_df <- data.frame(
  names=c("kim", "lee", "lim", "jo"),
  age=c(18, 20, 36, 44),
  sex=c("m", "f", "m", "f"),
  married=c(FALSE, FALSE, TRUE, TRUE),
  stringsAsFactors = FALSE)

phy_list[1]

#notes(31p)
library(dslabs)
head(murders)
murders$population
murders$pop
murders$to #구분할 수 있는 만큼 쳐주면 일부여도 보여준다, 걍 다 쳐라


#R01-26
install.packages("languageR")
library(languageR)
verbs
head(verbs) 
#I gave the book(Theme_NP) to John(Recipient_PP)
#I gave John it -> 이렇게 recipient가 짧아지면 3형식이 더 자연스러움.
#이런것처럼 length, animate 등이 문장의 자연스러움을 결정하는 요소가 됨. data based approach
#1
subset(verbs, Verb == "give" & verbs$AnimacyOfRec == "inanimate")
#2
verbs[(verbs$Verb =="give") & (verbs$AnimacyOfRec == "inanimate"),] #verb가 아니라 Verb // row에 해당하는 모든 cloumn을 보여달라!


#R01-27

chart_df <- data.frame(
  name=c("John", "Tammy", "Tim", "Jerry", "Carl", "Michael"),
  Age=c(35, 26, 48, 22, 39, 28),
  Position=c("Researcher", "Dealer", "CEO", "Sales", "Manager", "Sales"),
  Degree=c("Phd", "BA", "MBA", "BA", "MA", "BA"),
  Income=c(165000, 46000, 145000, 39000, 82000, 44000)
)
chart_df[order(chart_df$Position, -rank(chart_df$name)),]
#"Position", "Degree"
one <- subset(chart_df, select=c("Position", "Degree"))
one

#Calcultate Income
num <- order(chart_df$Age>30)
calcul <- mean(chart_df$Income[num],)
calcul

#least paid person
chart_df[(chart_df$Position != "Sales")&(chart_df$Income == min(Income))]

#subset(char_df, select=c("name", "Age"))

#R01-28
murders$rate <- murders$total / murders$population * 10^5
plot(murders$rate, murders$total, main = "My graph")
hist(murders$rate, title="Murder cases")
boxplot(rate~region, data = murders, 
        col=c("red", "blue", "green", "grey"))

#Two plots on one plane
par(mfrow=c(1,2)) # 1 row, 2 columns
boxplot(rate~region, data = murders)
hist(murders$rate)
par(mfrow=c(1,1)) #line 160 -> 원상복귀


#ggplot
install.packages("ggplot2")
library(ggplot2)
ggplot(data = murders) + geom_histogram(aes(x=population))



ve1 <- c(2, 3, TRUE, 4, 6, "HUFS")
ve1 <- as.numeric(ve1); ve1
ve2 <- c(2, 3, TRUE, 4, 6)
ve2 <- as.numeric(ve2);ve2

nums <- c(1,2,3,4,5,6,7)
nums[c(3,6)]


age <- c("baby", "kid", "adult")
age <- c(1,2,4,6,7)
age <- ordered(age);age

