# Contingency table in R
modal <- cbind(c(5500, 726), c(2211, 1903)) # matrix
rownames(modal) <- c("will", "begoingto")
colnames(modal) <- c("BE", "AE")

#Visualization
colors <- c("lightblue", "coral")
barplot(modal, col=colors, main="Modal", xlab="Variety", ylab="Frequency")
legend("topright", fill=colors, c("will", "be-going-to")) 

# Alternatively, try adding the argument ‘beside = TRUE
barplot(over, beside = TRUE, col=colors, main="Modal", xlab="Variety", 
        ylab="Frequency") #over, beside 이런거 잘못됐으니까 다시 올려두겠음.

#Calculating proportions of each variable
prop.table(modal) #전체를 더하면 1이 될 것임.

prop.table(modal, 1) # 각 row의 ratio를 보여줌

prop.table(modal, 2) # ratio, each column



install.packages("vcd")
library(vcd)
assocstats(modal)

chisq.test(modal)$expected
chisq.test(modal) #significant association : 영국인, 미국인 will & be going to --> 이걸 사용하는 방식이다르다!!(plain)

1-pchisq(1561.8, df=1)

#실습
over <- cbind(c(22,4), c(5,12)) #matrix
rownames(over) <- c("meta", "nonm")
colnames(over) <- c("acad", "conv")
over

#visualize
colors <- c("lightblue", "coral")
barplot(over, col=colors, main="over", xalb="Register", ylab="Frequency")
legend("topright", fill=colors, c("metaphoric", "nonmetaphoric")) 

#effect size
prop.table(over, 2) #아까 이게좀 괜찮았던듯(?)

#x^2
assocstats(over)
chisq.test(over)

#chi-squared(df=1) = 11.149, p<.001

