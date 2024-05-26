#One-sample test
soph <- c(3.5, 3.3, 2.8, 4.3, 4.0, 4.1, 3.3, 3.6, 4.1, 2.4, 3.7, 3.8, 3.9, 2.8, 3.7, 3.9, 2.8, 3.0, 4.4, 3.5)
t.test(soph, mu = 3.30) #non-hypothesis를 reject할 수 없다.

ca <- c( 1773, 1765, 1771, 1758, 1729, 1740, 1772)
t.test(ca, mu=1775) #p value = 0.04546 -> reject가능한 수준, national average에 못미친다.(reject한 것)
#1775 1748 (평균에 못미치는 결과다)
#학생들의 평균 장학금? 이런 것들을 구할 때 유용한 계산

library(dplyr)
library(languageR)
durationsOnt %>% head
new <- durationsOnt$DurationOfPrefix
  
t.test(new, mu = 0.156)
#해석 : 

#53
am = c(144, 147, 148, 172, 170, 133, 141, 144, 146); mean(am)
pm = c(133, 138, 139, 160, 165, 133, 140, 142, 144); mean(pm) #평균 떨어짐 --> 이차이가 중요하냐?
boxplot(am, pm)
plot(density(am), col="red")
lines(density(pm), col="blue")
t.test(am,pm,paired = TRUE) #2개니까 paired, false가 default
#--> 중요하다. mean of diff = 5.6

delta <- am-pm
t.test(delta, mu=0) #p 똑같음 --> paired ttest는 one sample이랑 다를게 없다.



library(lattice)
bwplot(Frequency ~ Class | Complex, data=ratings)
# extract relevant rows with the value "simplex" of Class
sim = ratings[ratings$Complex == "simplex", ] #value가 simplex, column이랑 헷갈리지 말고
com = ratings[ratings$Complex == "complex", ]
sim
com

# extract relevant rows of sim with the value of “animal” and “plant”
freq_animal = sim[sim$Class == "animal", ]$Frequency
freq_plant = sim[sim$Class == "plant", ]$Frequency
freq_animal

# perform t-test and check the result
t.test (freq_animal, freq_plant)


#,ANOVA
#r syntax: plot (response ~ factor, data)
score = c(13.1, 15, 14, 14.4, 14, 11.6, 16.3, 15.7, 17.2, 14.9, 14.4, 17.2, 13.7, 13.9, 12.4, 13.8, 14.9, 13.3) # read in the data
group = c(rep("ke", 6), rep("kn", 6), rep("en", 6))
md = data.frame(score, group)
plot(score ~ group, data=md)

#r syntax: aov(response ~ factor, data)
md.aov = aov (score ~ group, data=md)
summary (md.aov)

#17
score = c(13.1, 15, 14, 14.4, 14, 11.6, 16.3, 15.7, 17.2, 14.9, 14.4, 17.2, 13.7, 13.9, 12.4, 13.8, 14.9, 13.3, 15.7, 13.7, 14.4, 16, 13.9, 14.7, 13.5, 13.4, 13.2, 12.7, 13.4, 12.3) # read in the data
group = c(rep("ke", 6), rep("kn", 6), rep("en", 6), rep("ee", 6), rep("ks", 6))
md = data.frame(score, group)

md <- data.frame(score, group)
md%>%head
boxplot(score~group, md)
md.aov = aov (score ~ group, data=md)
summary(md.aov)

pairwise.t.test(score, group, p.adjust = "bonferront") #이게 더 보수적(TurkishhSD 보다) _ Turkish를 더 선호, 더 달라 보이니까???
TukeyHSD(md.aov, conf.level = 0.95)

#T
t.test(ke, kn)
#ANOVA
md2 <- subset(md, group =="ke" | group == "kn")
md2.aov<- aov(score~group, data=md2)
summary(md2.aov) #2 sample--> correction 필요 없다는걸 보여주는 중

#19p
a <- c(4, 5, 4, 3, 2, 4, 3, 4, 4)
b <- c(6, 8, 4, 5, 4, 6, 5, 8, 6)
c <- c(6, 7, 6, 6, 7, 5, 6, 5, 5)
drug_md <- data.frame(a,b,c)
drug_md.aov = aov(a~c, data=drug_md)
summary(drug_md.aov)
pairwise.t.test()
