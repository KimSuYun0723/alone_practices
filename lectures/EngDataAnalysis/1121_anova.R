#HY_1_new
library(languageR)
md <- subset(ratings, select = c("Word", "Frequency", "Class", "meanWeightRating", "meanSizeRating"))
head(md)

skewness(md$meanSizeRating)
skewness(md$meanWeightRating)
#하지만 정교하게 normality를 판단할 필요가 있음
#bi-modelity 처리못함. : ^^ 이렇게 생긴 분포 --> normal하지 않은데, skewness가 0이 나올 것임.
#숫자의 정확한 기준 X : 숫자로 나오는데(2.31같은), 이 기준이 너무 주관적임. 0.98은 normal한지 아닌지 기준이 정확지 않은 한계.


#HY_2_new_22
size <- md$meanSizeRating
weight <- md$meanWeightRating
shapiro.test(size) #p-value = 2.05e-05 --> 너무 작아. normal하지 않음
shapiro.test(weight)#p-value = 4.482e-05 --> 얘도 마찬가지.
#이렇게 normal하지 않으면 non-paramatric t.test 해야함함

par(mfrow=c(1,2))
boxplot(weit, size, names=c("weight", "size"), ylab = "mean rating")
boxplot(weit-size, md$meanSizeRating, ylab="mean rating difference")
par(mfrow=c(1,1))

shapiro.test(size-weight) #이게 더 적절함. 뭐가 더 먼저 오는진 상관없음._p-value = 0.02374 --> 0.01이라고 본다면 normal. 2가지 방법 둘다 가능
t.test(size, weight, paried = TRUE)


#non-paramatric t.test
wilcox.test(weight, size, paired=TRUE) #p-value = 5.463e-15 --> 길이가 많이 나온다고 해서 무게가 많이 나오는 것은 아니다!! 라는 결론


CA <- c(1773, 1765, 1771, 1758, 1729, 1740, 1772, 1639, 1654, 1823, 1998)
shapiro.test(CA)


#ANOVA--> HT2
score = c(13.1, 15, 14, 14.4, 14, 11.6, 16.3, 15.7, 17.2, 14.9, 14.4, 17.2, 13.7, 13.9, 12.4, 13.8, 14.9, 13.3, 15.7, 13.7, 14.4, 16, 13.9, 14.7, 13.5, 13.4, 13.2, 12.7, 13.4, 12.3) # read in the data
group = c(rep("ke", 6), rep("kn", 6), rep("en", 6), rep("ee", 6), rep("ks", 6))
md <- data.frame(score, group)

shapiro.test(subset(md$score, md$group == "ee")) #p-value = 0.4768 --> normal. noramlity 통과
#이제 homogenious 한지 체크해야함
fligner.test(score ~ group, data = md) #homo는 여러개를 같이 체크하는거라서, syntax가 달라짐. group이 Y(predict) 에 있어야 함.
#H0이 homo하다 라는 것. p-value = 0.3752 --> anova를 진행해도 되는 것이다~

#만약 homogenouty가 확보가 안되면!
oneway.test(score ~ group, data = md)  #anova로 전향한다...?


#25
#Check normality and homogeneity of the data ‘speech-rate.csv’ of the task S04-  03b -HW
#HW : S04-  03b + 25p
#아노마, 호모 뭐시기 테스트를 하고, 데이터가 통과되거나 안되면 non-paramatric ... 스스로 판단해서 해봐라
md2<- read.csv((file.choose()))

#26
#non-normal distrubution. anova랑 똑같이 해석할 수 있음
kruskal.test (response ~ predictor, data)

