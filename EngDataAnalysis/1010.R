install.packages("installr")
library(installr)
updateR()

Sys.getenv("R_HOME") #where R installed
Sys.getenv("HOME") #User's home directory
getwd() #working directory : the project's home directory

#.Rprofile -> R 열때마다 설치해줄 것들을 넣어두는
library(dplyr)
library(dslabs)
library(languageR)

options(prompt="jty >") #한번 해봐라


check_length <- function(x) {
  len <- nchar(x)
  if (len < 5) {
    message <- "short"
  } else if (len <9) {
    message <- "medium"
  } else {
    message <- "long"
  }
    cat (paste(len, ": ", message, sep="")) #space 붙게 하려면 
}

murders %>% head
murders$size <- ifelse(murders$population > 10^6, "big", "small")

verbs %>% head
verbs$Length <- ifelse(verbs$LengthOfTheme >=1.5, "long", "short")


par(mfrow=c(3,3))
for (i in 1:9) {
  hist(rnorm(100),
  main=paste("Trial", i, sep = " "))
}
par(mfrow=c(1,1))


#Task R05-01
years <- c(2023:2100)
for (y in years) {
 if (y %% 4 ==0) {
   print(y)
 } 
}

#Task R05-02
words <- c("red", "yellow", "blue", "white", "purple", "navyblue")

for (c in words) {
  cat("The word", c, "has", nchar(c), "characters\n")
}

score <- c(13.1, 15, 14, 14.4, 14, 11.6, 16.3, 15.7, 17.2, 14.9, 14.4, 17.2, 13.7, 13.9, 12.4, 13.8, 14.9, 13.3, 15.7, 13.7, 14.4, 16, 13.9, 14.7, 13.5, 13.4, 13.2, 12.7, 13.4, 12.3) 
group <- c(rep("ke", 6), rep("kn", 6), rep("en", 6), rep("ee", 6), rep("ks", 6))
md <- data.frame(score, group)
md
library(dplyr)

gnames <- unique(group)
for (g in gnames) {
  cat(g, ":", mean(which(md$group==g)), "\n")
}


  #prof
#no for
md %>% head
md[md$group == "ke", ]$score %>% mean()
md[md$group == "ke", ]$score %>% sd %>% round(2)
md[md$group == "kn", ]$score %>% mean()
md[md$group == "kn", ]$score %>% sd %>% round(2)

#yes for
gnames <- unique(group)
n <- length(gnames)

for (i in 1:n) { #numeric 하게 접근하기 위해서는 이렇게 index
  mv <- subset(md$score, md$group == gnames[i])
  mean <- mean(mv); sd <- sd(mv)
  cat(gnames[i], ":", "mean", mean, "sd", sd, "\n")
}

apply(md, 2, mean) #간단한 작업을 위해 유용. 하지만 그렇게까지 generic하지는 않음.


