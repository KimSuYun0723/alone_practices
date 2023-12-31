library(languageR)
md <- subset(ratings, select = c("Word", "Frequency", "Class", "meanWeightRating", "meanSizeRating"))
head(md)

#오늘의 주가가 내일의 주가에 완전히 dependent하진 않음
#어떤 v와 다른 v의연계성은 특수해질때가 많은데
#t는 전혀 판단하지 못함
#두 v의 연관성을 파악하는 것 - correlation
#하지만 한계가있음
#두 변수간 관계를 밀접하게 확인해주지 못함. 기울기("얼마나 더 밀접한지) 등에 대한 정보는 알 수가 없음

lm.ratings <- lm(md$meanSizeRating ~ md$meanWeightRating, data= ratings)
coef(lm.ratings)

plot(ratings$meanWeightRating, ratings$meanSizeRating, col="red")
abline(0.527, 0.926)

mypredict <- function(x) {
  y <- 0.9265*x +0.5270
  cat(y)
}
mypredict(2.5)

am = c(144, 147, 148, 172, 170, 133, 141, 144, 146, 148, 152, 149, 143, 138, 165, 143, 142, 155, 135, 144)
pm = c(133, 138, 139, 160, 165, 133, 140, 142, 144, 142, 139, 144, 139, 130, 164, 140, 128, 129, 133, 144) 
# What will be the evening pitch of a person whose morning pitch is 128 Hz.
am.ratings <- lm(pm~am);am.ratings
plot(am, pm)
abline(am.ratings)
summary(am.ratings)

  #student
lm.pitch <- lm(pm~am)

plot(pm~am)
abline(lm.pitch)

new.am <- data.frame(am=128)
new.pm <- predict(lm.pitch, new.am)
new.pm #124.8(128에서 3점도 떨어진다~)
#물론 데이터가 적어서 reliability는 믿을게 못되지만
#이런식으로 이루어진다~
summary(lm.pitch)
  
  #
res.ratings<- resid(am.ratings)
plot(am,res.ratings)
abline(0,0)
