# S04-03b: ANOVA
#speech-rate.csv
#Analyze the data given and make a report on their speech rate focusing on the differences between the employee types.
#Submit your report in (pdf/docx/hwpx) format with the R code attached at the end

#data
data <- read.csv(file.choose())
comedian <- subset(data, data$type =="comedian")$rate ;comedians
casters <- subset(data, data$type =="sports caster")$rate ;casters
anchors <- subset(data, data$type =="news anchor")$rate ;anchors
actors <- subset(data, data$type =="drama actor")$rate ;actors

value <- c(comedian, casters, anchors, actors);value
group = c(rep("Comedians", 15), rep("Sports casters", 15), rep("News anchors", 15), rep("Drama actors", 15))
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
oneway.test(value~group, data = df)#F = 7.8119 p-value = 0.0005379
df.oneway <- oneway.test(value~group, data = df)
#TukeyHSD
TukeyHSD(df.oneway, conf.level=0.95)
#                                   diff        lwr         upr     p adj
#Drama actors-Comedian       -0.51333333 -0.8714241 -0.15524253 0.0020090
#News anchors-Comedian       -0.37333333 -0.7314241 -0.01524253 0.0379017
#Sports casters-Drama actors  0.44000000  0.0819092  0.79809080 0.0101493

#Sports casters-Comedian     -0.07333333 -0.4314241  0.28475747 0.9482432
#News anchors-Drama actors    0.14000000 -0.2180908  0.49809080 0.7296144
#Sports casters-News anchors  0.30000000 -0.0580908  0.65809080 0.1307849


#####t.test 시각화
library(ggplot2)

# Tukey 다중 비교 결과를 데이터프레임으로 정리
tukey_results <- data.frame(
  Comparison = c("Drama actors-Comedian", "News anchors-Comedian", "Sports casters-Comedian",
                 "News anchors-Drama actors", "Sports casters-Drama actors", "Sports casters-News anchors"),
  Difference = c(-0.51333333, -0.37333333, -0.07333333, 0.14000000, 0.44000000, 0.30000000),
  Lower = c(-0.8714241, -0.7314241, -0.4314241, -0.2180908, 0.0819092, -0.0580908),
  Upper = c(-0.15524253, -0.01524253, 0.28475747, 0.49809080, 0.79809080, 0.65809080),
  P_Adj = c(0.0020090, 0.0379017, 0.9482432, 0.7296144, 0.0101493, 0.1307849)
);tukey_results

# 바 그래프로 시각화
ggplot(tukey_results, aes(x = Comparison, y = Difference)) +
  geom_bar(stat = "identity", aes(fill = P_Adj < 0.05), position = "dodge") +
  geom_errorbar(aes(ymin = Lower, ymax = Upper), width = 0.2, position = position_dodge(0.9)) +
  labs(title = "The Result of Tukey's HSD test", y = "Difference of average") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))


##########바 그래프로로(유의미한 것만만)
tukey_results <- data.frame(
  Comparison = c("Drama actors-Comedian", "News anchors-Comedian", "Sports casters-Comedian",
                 "News anchors-Drama actors", "Sports casters-Drama actors", "Sports casters-News anchors"),
  Difference = c(-0.51333333, -0.37333333, -0.07333333, 0.14000000, 0.44000000, 0.30000000),
  P_Adj = c(0.0020090, 0.0379017, 0.9482432, 0.7296144, 0.0101493, 0.1307849)
)

# 유의미한 차이를 가진 그룹 쌍 필터링
significant_pairs <- tukey_results[tukey_results$P_Adj < 0.05, ]

# 막대 그래프로 시각화
barplot(significant_pairs$Difference, names.arg = significant_pairs$Comparison,
        col = ifelse(significant_pairs$Difference < 0, "blue", "red"),
        main = "Meaningful Result of Tukey's HSD", ylab = "Difference of average")

