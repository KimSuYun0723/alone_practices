ldt<- read.csv(file.choose())
md <- ldt
leng <- md$Length
freq <- log1p(md$Freq);freq
rt <- log1p(md$Mean_RT);rt

### Linear modeling
lm.both = lm(rt ~ freq + leng, data=md) #R_squared : 0.5184 (hw09 파일에 freq로만 갖고 만든 0.39보다 높음.)
#변수 1개보다, multiple regression이 더 설명을 잘함. 물론 아직 5.1도 부족한거긴하지.
#standard error도 줄었음.
summary(lm.both) #leng, freq 둘다 유의미하다(highly significant!!)
#FORMULA : log1p(rt) = -0.0277*log1p(freq) + 0.0297*leng + 6.5931

new.word3 <- data.frame(leng=6, freq=log1p(19))
exp(predict(lm.both, new.word3))-1

#S05-04
#length model 만 갖고 하면 :719
#freq model : 890
#both : 801 --> 얘가 더 정확하다~



library(languageR); data(ratings)
ratings %>% head
plot(ratings$FreqSingular, ratings$FreqPlural)
abline(lm(FreqPlural ~ FreqSingular, data = ratings), col="red")

# after removing outliers
ratings.x = subset (ratings, ratings$FreqSingular < 500) # cut-off outliers
abline(lm(FreqPlural ~ FreqSingular, data=ratings.x), col="green")


#more robust regression technique with respect to outliers.
library(MASS)
abline(lmsreg(FreqPlural ~ FreqSingular, data=ratings), col="blue")
#lmsreg : linear modeling regression 어쩌구

# after log transformation
#outlier를 무작정 삭제하면 안돼. too much data loss 야기
#잘라낼 것이 아니고, transformation해야할 것이다.
plot(log1p(ratings$FreqSingular), log1p(ratings$FreqPlural))
abline(lm(log1p(FreqPlural) ~ log1p(FreqSingular), data=ratings), col="red")
abline(lmsreg(log1p(FreqPlural) ~ log1p(FreqSingular), data=ratings), col="blue")


#Should it be linear?
lm.ratings = lm(meanSizeRating ~ meanFamiliarity, data=ratings)
round(summary(lm.ratings)$coef, 3)

# Base
plot(ratings$meanFamiliarity, ratings$meanSizeRating, type="n") 
plants = ratings[ratings$Class == "plant",] # class specific
animals= ratings[ratings$Class == "animal",] # class specific

# adding the points with the scatterplot smoother function lowess().
points(plants$meanFamiliarity, plants$meanSizeRating, pch='p', col="green") #pch뭐임
lines(lowess(plants$meanFamiliarity, plants$meanSizeRating),col="blue")
#가장 낮은 standard error 기준으로 선을 그려봄. 직선 아니고
points(animals$meanFamiliarity, animals$meanSizeRating, pch='a', col="red")
lines(lowess(animals$meanFamiliarity, animals$meanSizeRating),col="purple")

# Linear modeling & linear regression lines
lm.plants = lm(meanSizeRating ~ meanFamiliarity, plants)
lm.animals = lm(meanSizeRating ~ meanFamiliarity, animals)

abline(coef(lm.plants), col="blue", lty=2)
abline(coef(lm.animals), col="purple", lty=2)
#직선이 아닌 곡선이 잘 설명해주는 것같다!!
#과연 y= ax+b 이라는 linear한 직선이 이 모델을 잘 설명할 수 있을까.
#그렇다고 이 라인을 완전히 무시하기엔... 왜냐하면 전체적인 트랜드는 보여주고 있음
#곡선과 직선 양쪽을 다 보고 싶은 것.
#+) 직선으로 표현하기 어려운 것들은 ^2으로 표현함.(2차 함수는 직선으로 표현 못하잖아)

#quadratic term 을 추가하면 됨.(2차항. ax^2)
#왜냐 : 직선과 곡선 모두를 보고 싶으니까! ax^2+bx+c 이런식으로.
lm.plants = lm(meanSizeRating ~ meanFamiliarity + I(meanFamiliarity^2), data=plants) # Note the function I()
#I는 뭐냐면.. lm이라는 함수 안에 ^2를 못넣기 때문에, 벗어날 수 있게 해주라고 I를 넣은 건데...뭐~
summary(lm.plants)$coef
#훌륭한 모델은 아닌데, R squared 랑 error 생각해보면 나아지긴 했어.

#new graph
plot(ratings$meanFamiliarity, ratings$meanSizeRating, type="n")
points(plants$meanFamiliarity, plants$meanSizeRating, pch='p', col="green")
plants$predict = predict(lm.plants) # get each response coordinate
plants=plants[order(plants$meanFamiliarity), ] # sorting
lines(plants$meanFamiliarity, plants$predict, col="blue")


