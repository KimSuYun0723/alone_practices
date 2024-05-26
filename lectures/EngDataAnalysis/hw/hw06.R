# S02-09
data <- read.csv(file.choose()) ; data
zscore <- function(x, data){
  z_x <- (x-mean(data))/sd(data)
  return (z_x)
}

a <- data$Type_A
z_a <- zscore(122, a) ; z_a
b <- data$Type_B
z_b <- zscore(136, b) ; z_b
c <- data$Type_C
z_c <- zscore(108, c) ; z_c

name <- c("John","Ted","Jerry"); name
choose <- c(z_a, z_b, z_c) ; choose
answer <- name[which(choose == max(choose))];answer
cat("The most intelligent person is",answer)


# S01-11

#Work with 'ldt' data
ldt <- read.csv(file.choose()) ; ldt
ldt
install.packages("moments")
library(moments)
library(dplyr)

#Verify visually whether word frequency affects response duration
mdf1 <- log(ldt$Freq)
mdr1 <- log(ldt$Mean_RT)
plot(x = mdf1, y = mdr1, ylab ="Response duration", xlab = "Freqency", type = "p")

#Transform the data distribution when necessary
mdf2 <- log1p(ldt$Freq)
mdr2 <- log1p(ldt$Mean_RT)
plot(x = mdf2, y = mdr2, ylab ="Response duration", xlab = "Freqency", type = "p")
 