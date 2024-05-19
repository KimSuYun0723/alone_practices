#Task S05-06
#[version 2] Consider two variables of the data 'ratings': 'meanSizeRatings' and 'meanFamiliarity'.
library(languageR); data(ratings)
head(ratings)
animal <- subset(ratings, ratings$Class=="animal"); animal
size <- animal$meanSizeRating; size
fam <- animal$meanFamiliarity; fam

#The question is: Hot to predict the size of an 'animal' object based on its familiarity.
#Check the distribution of the relevant data.
library(moments)
hist(size); skewness(size)
hist(log1p(size)); skewness(log1p(size))
hist(fam); skewness(fam)
hist(log1p(fam)); skewness(log1p(fam)) #need log1p

#Check normality
shapiro.test(size)#p-value = 0.5015
shapiro.test(fam)#p-value = 0.0722
shapiro.test(log1p(fam))#p-value = 0.5616

#Construct competing linear models: one with a plane predictor term
lm.size1 <- lm(size~log1p(fam));lm.size1
par(mfrow=c(1,1))
plot(size~log1p(fam))
abline(lm.size1)

#Construct competing linear models: the other with an additional quadratic term.
# adding the points with the scatterplot smoother function lowess().
points(log1p(fam),size, pch='p', col="red") 
lines(lowess(log1p(fam),size), col="purple")
lm.size2 <- lm(size ~ log1p(fam) + I(log1p(fam)^2), data=animal)

#new graph
plot(log1p(fam), size, type="n")
points(log1p(fam), size, pch='p', col="green")
animal$predict <- predict(lm.size2) 
ani_size <- animal[order(log1p(fam)), ] 
lines(log1p(fam), animal$predict, col="blue")

#Compare the models and determine which one better accounts for the data.
summary(lm.size1) # standard error: 0.4168, Multiple R-squared:  0.1803
summary(lm.size2) # standard error: 0.3963, Multiple R-squared:  0.276
#standard error and R-squared are improved 
#model with an additional quadratic term ==> better

#Using the model, predict what will be the size rating score when a meanFamiliarity score is '3.98'
new.fam <- data.frame(fam=log1p(3.98)); new.fam
new.size <- predict(lm.size2, new.fam); new.size

#실제로 그러한지 체크해보기
ans <- subset(animal, (animal$meanFamiliarity<4)&(animal$meanFamiliarity>3))$meanSizeRating;ans
mean(ans) #3.562921 _quite similar
median(ans) #3.598_ quite similar


#Task R06-02:
#Use the built-in variable 'state.name'
data <- state.name

#Print out all the U.S. state names starting with "New"
new <- subset(data, grepl("^New", data));new

#Print out all the U.S. state names consisting of multiple words
multi <- subset(data, grepl("[a-zA-z]+ [a-zA-z]+", data));multi

#Print out all the U.S. state names convert all letters of 's' or 'S' into '$'
s <- gsub("[Ss]", "$", data);s