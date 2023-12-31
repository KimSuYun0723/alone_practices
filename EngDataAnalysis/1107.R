md <- read.csv(file.choose())
md

L1 <- md[md$Proficiency=="L1",]$Rate
L2 <- md[md$Proficiency=="L2",]$Rate

mean(L1); sd(L1)
mean(L2); sd(L2)
par(mfrow=c(2,2))
hist(L1, breaks = 6, xlim = range(3,8)) #scale이 다르니까 3~8까지 보여주는것으로 맞춰줌
boxplot(L1, ylim = range(3,8), horizontal = TRUE) #뒤집었으니까 ylim
hist(L2, breaks = 8, xlim = range(3,8)) #breaks는 막대를 몇개 만들 것인가? 얘는 넓어서 8개 정도로 하면 비슷해짐 위아래가
boxplot(L2, ylim = range(3,8), horizontal = TRUE)
par(mfrow=c(1,1))
  #density도 그려보고 싶고.. 색깔도 바꿔보고 싶고.. 등등 visualization 너무 중요해

#16p
A <- c(22,35,38,41)
B <- c(7000, 10000, 12000, 15000)
c <- cov(A,B)
c #26333.33 --> 큰 숫자들을 갖고 있으니 당연히 크게 나오지
  #cm에서 mm, g에서 mg 바꿨잖아 단위를 잘 봐야지
  #같은 데이터인데 단위 바꿨다고 이렇게 차이가나
  #covariance가 잘못됐다는 말이 아니라, covariance를 direct로 적용시키는데에 한계가 있다는 말.

ldt <- read.csv(file.choose())
ldt

cor(ldt$Length, ldt$Mean_RT)
cor(ldt$Freq, ldt$Mean_RT)
#cor.test --> p-value 등 정보를 다 보여줌

age = c(20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40)
pitch = c(144, 145, 143, 140, 144, 139, 141, 139, 138, 189, 141) #p = 0.3829 --> 이정도의 차이는 통게적으로 유의미하다고 보지 않음
#그래서 우리가 눈으로 보는 차이와 통계에서 말하는 차이는 다른 것임.
cor.test(age, pitch)


#31p
cor(ldt$Length, ldt$Mean_RT) #0.61
library(moments)
skewness(ldt$Length) #0.14 _ log를 씌운다고 더 증가할 것 같지 않음. 씌우면 -0.55.. 오히려 악화됨
skewness(ldt$Mean_RT) #1.28
skewness(log1p(ldt$Mean_RT)) #0.5로 더 개선됨
cor(ldt$Length, log1p(ldt$Mean_RT)) #0.62
cor(ldt$Freq, log1p(ldt$Mean_RT)) #-0.4
cor(log1p(ldt$Freq), log1p(ldt$Mean_RT)) #-0.62 훨씬 많이 개선됨
#cor 한계 : y축으로 얼마나 증가하는지는 볼수가 없음. --> linear.. 어쩌구. 그떄가서 correlation을 다시 보게 될거야


