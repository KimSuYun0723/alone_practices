# S04-03b: ANOVA

#data
data <- read.csv(file.choose())
comedian <- subset(data, data$type =="comedian")$rate ;comedians
casters <- subset(data, data$type =="sports caster")$rate ;casters
anchors <- subset(data, data$type =="news anchor")$rate ;anchors
actors <- subset(data, data$type =="drama actor")$rate ;actors

value <- c(comedian, casters, anchors, actors);value
group = c(rep("Comedians", 15), rep("Sports casters", 15), 
          rep("News anchors", 15), rep("Drama actors", 15))
df <- data.frame(value, group);df

#Show visually
library(lattice)
bwplot(value~group, data = df)

#check normality
library(moments)

skewness(comedian); skewness(log1p(comedian)) #log1p is improved
skewness(casters); skewness(log1p(casters)) #log1p is improved
skewness(anchors); skewness(log1p(anchors)) #log1p is improved
skewness(actors); skewness(log1p(actors)) #log1p is improved

par(mfrow=c(2,2))
hist(comedian) 
hist(casters)
hist(anchors)
hist(actors)

par(mfrow=c(2,2))
hist(log1p(comedian))
hist(log1p(casters))
hist(log1p(anchors))
hist(log1p(actors))


shapiro.test(comedian)#p-value = 0.7853
shapiro.test(log1p(comedian))#p-value = 0.7994

shapiro.test(casters) #p-value = 0.3825
shapiro.test(log1p(casters))#p-value = 0.4258

shapiro.test(anchors) #p-value = 0.3478
shapiro.test(log1p(anchors))#p-value = 0.4411

shapiro.test(actors) #p-value = 0.7593
shapiro.test(log1p(actors))#p-value = 0.8077

#check homogeneous
fligner.test(value ~ group, data = df) #p-value = 0.01204

#test
oneway.test(value~group, data = df)#F = 7.8119, p-value = 0.0005379


#PROF


