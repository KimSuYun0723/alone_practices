#S05-03b
ldt <- read.csv(file.choose())
freq <- ldt$Freq ; freq
leng <- ldt$Length; leng
rt <- ldt$Mean_RT; rt

#check normality
skewness(freq); skewness(log1p(freq))#need log1p
skewness(leng); skewness(log1p(leng))
skewness(rt); skewness(log(rt))#need log1p

shapiro.test(log1p(freq))#p-value = 0.1699
shapiro.test(leng)#p-value = 0.08559
shapiro.test(log1p(rt))#p-value = 0.05442

#linear regression
par(mfrow=c(1,1))
lm.freq <- lm(log1p(rt)~log1p(freq));lm.freq
lm.leng <- lm(log1p(rt)~leng);lm.leng
plot(log1p(rt)~log1p(freq))

abline(lm.freq)

#6word
new.leng <- data.frame(leng=6);new.leng
new.rt <- predict(lm.leng, new.leng);new.rt
exp(new.rt)




#PROF
freq <- log1p(ldt$Freq) ; freq
leng <- ldt$Length; leng
rt <- log1p(ldt$Mean_RT); rt

cor(rt, leng); cor(rt, freq)

lm.leng = lm(rt~leng, data =ldt);summary(lm.leng)

#Intercept : b가 0은 아니다. intercept가 필요하다 라는 것.

lm.freq = lm(rt~freq, data=ldt);summary(lm.freq)

plot(leng,rt); abline(lm.leng, col="red")
plot(freq,rt); abline(lm.leng, col="blue")

install.packages("rgl") #3차원 패키지지
library(rgl)
colors <- c("red", "blue", "coral")
plot3d(
  x = leng, y = freq, z = rt, 
  col = colors, type = 's', radius= .15,
  xlab = "length", ylab = "Frequency", zlab = "Reaction Time(ms)"
)

new.word <- data.frame(leng=6)
new.rt <- predict(lm.leng, new.word)
print(new.rt)
exp(new.rt)-1
#log1p는 1+된거니까 -1

new.word2 <- data.frame(leng=6)
new.rt2 <- prediction()

md2<- subset(ldt, ldt$Length ==6)
mean(md2$Mean_RT) #719(predcition) similar
#근데 이모델만으로는 부족해. 왜냐면 freq도 rt에 영향을 미치기 때문에..

new.word2 <- data.frame(freq=150)
new.rt2 <- predict(lm.freq, new.word2)
print(new.rt2)
exp(new.rt2)-1 #0.815 -> 이상하지 않아?
#X(freq)에도 log가 있어서 벗겨내야 하잖아.
#--> 어떻게 하면 좋을까? model에서 벗겨야 할까 어디서 벗어야 할까
new.word2 <- data.frame(freq=log1p(150)) #값을 넣을 때 log를 넣어어
new.rt2 <- predict(lm.freq, new.word2)
print(new.rt2)
exp(new.rt2)-1


new.word2 <- data.frame(leng=6)
new.rt2 <- prediction()

md2<- subset(ldt, ldt$Length ==6)
mean(md2$Mean_RT)

x=3.3
a<- log1p(x)
exp(a)
