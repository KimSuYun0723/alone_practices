# Task R01-31
library(languageR)
library(dplyr)
head(verbs)
lang <- subset(verbs, verbs$Verb == "give") ; lang

group <- unique(lang$RealizationOfRec); group
np_av <- subset(lang, lang$RealizationOfRec == group[1])$LengthOfTheme %>% mean; np_av
pp_av <- subset(lang, lang$RealizationOfRec == group[2])$LengthOfTheme %>% mean; pp_av

if (np_av > pp_av) {
  cat("Conclision: \n", "The higher LengthOfTheme is, the higher the possibility that NP is coming after verb 'give'")
} else if (np_av < pp_av) {
  cat("Conclision: \n", "The higher LengthOfTheme is, the higher the possibility that PP is coming after verb 'give'")
} else {
  cat("Conclision: \n", "They has a same average of LengthOfTheme")
}
#I gave him the book (theme-the book-이 길어지면 뒤에 나오고 싶어함)
#I gave the book to him 
#일반화하기에는 data 개수가 너무 작고
#NP PP 는 length of theme만으로 결정되지는 않으므로;;
# 값의 차이가 과연 유의미한가?


#Optional Task
lang <- subset(verbs, verbs$Verb == "give") ; lang

oo <- subset(lang, lang$AnimacyOfRec == "animate" & lang$AnimacyOfTheme == "animate")$LengthOfTheme %>% mean
oo # 1.978298
ox <- subset(lang, lang$AnimacyOfRec == "animate" & lang$AnimacyOfTheme == "inanimate")$LengthOfTheme %>% mean
ox # 1.757592
xo <- subset(lang, lang$AnimacyOfRec == "inanimate" & lang$AnimacyOfTheme == "animate")$LengthOfTheme %>% mean
xo # 2.639057 (longest LengthOfTheme)
xx <- subset(lang, lang$AnimacyOfRec == "inanimate" & lang$AnimacyOfTheme == "inanimate")$LengthOfTheme %>% mean
xx # 1.106522 (shortest LengthOfTheme)

# R\T     O          X
# O : 1.978298   1.757592
# X : 2.639057   1.106522
#If AnumacyOfTheme is in animate, "LengthOfTheme is low.
#NP PP 일때 inanimate, animate 의 개수 비교할수도 있겠지
#숫자 자체가 bias가 있음. (기본적으로 animate가 더 많을 것임)
#턱없이 부족한 data


# Task R04-03 
is_leap <- function(year) {
  if (year %% 100 == 0) {
    if (year %% 400 ==0) {
      cat(paste("TRUE\n", "Yes, the yea r", year, " is a leap year", sep =""))
    } else {
      cat(paste("FALSE\n", "No, the year ", year, " is not a leap year", sep =""))
    }
  } else if (year%%4 ==0) {
    cat(paste("TRUE\n", "Yes, the year ", year, " is a leap year", sep =""))
  } else {
    cat(paste("FALSE\n", "No, the year ", year, " is not a leap year", sep =""))
  }
}

is_leap(2012)
is_leap(2401)
