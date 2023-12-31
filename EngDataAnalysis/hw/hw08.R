#S03-14
#Probelm 1. Does the complex word appear less frequently than simplex word?
  #[Data]
library(languageR)
data(ratings)
head(ratings)
simf = ratings[ratings$Complex == "simplex", ]$Frequency
comf = ratings[ratings$Complex == "complex", ]$Frequency

  #[Descriptive statistics]
summary(simf)
summary(comf)

  #[Hypothesis]
#H0: There is no difference in frequency between the two groups, complex and simplex words. 
#HA: There is a significant difference in requency between the two groups, complex and simplex words. 

  #t-test
t.test(simf,comf)

  #[report]
#There was a significant difference in frequency between complex and simplex words. 
#The independent t-test result indicates that the frequency of simplex word was higher (t(12.62) = 3.1652, p < 0.01).

  #[interpretation]
#As p-value is lower than 0.01, H0 should be rejected and HA is adopted instead. 
#In other words, the complex word appear less frequently than simplex word.



#Problem 2. Do words appear in the singular form more frequently than in the plural form?
freq_sing = ratings$FreqSingular
freq_plu = ratings$FreqPlural

  #[Descriptive statistics]
summary(freq_sing)
summary(freq_plu)

#[Hypothesis]
#H0: There is no difference in frequency between the two types of words, singular and plural form.
#HA: The frequency of words of singular form is not the same as the plural form.

  #t-test
t.test(freq_sing, freq_plu, paired = TRUE)

  #[report]
#There was no significant difference in in frequency between two types of words, singular and plural form (t(80)=1.5221, p = 0.1319), 

  #[interpretation]
#As p-value is greater than 0.05, H0 should be kept.
#That is, the difference in frequency between singular and plural form is not significant.


pl <- ratings$FreqPlural
sg <- ratings$FreqSingular

library(moments)
skewness(pl);skewness(log1p(pl))
skewness(sg);skewness(log1p(sg))

t.test(log1p(pl), log1p(sg), paired = TRUE) # improved. log값 보고 나서 ㄱㄱ


#S03-15
  #Problem : Is the difference in the average word lengths from fiction and non-fiction meaningful?
fic <- c(4, 5, 6, 5, 7, 4, 5, 6, 5, 6, 7, 5, 6, 4, 7, 8, 5, 6, 4, 5, 6, 7, 8, 6, 5, 4, 7, 6, 5, 8)
non_fic <- c(5, 6, 7, 8, 6, 5, 4, 7, 6, 5, 8, 4, 5, 6, 5, 7, 4, 5, 6, 5, 6, 7, 5, 6, 4, 7, 8, 5, 6, 4)

  #[Descriptive statistics]
summary(fic)
summary(non_fic)

  #[Hypothesis]
#H0: There was no significant difference in the average word lengths from two different genres of writing, fiction and non-fiction.
#HA: There is a significant difference in the average word lengths from two different genres of writing, fiction and non-fiction.

  #t-test
t.test(fic, non_fic) #p-value = 1 

  #[report]
#There was no significant difference in the average word lengths from two different genres of writing, fiction and non-fiction (t(58)= 0, p = 1), and 
#and also, the each means are equal (5.73333 = 5.73333).

  #[interpretation]
#As p-value is greater than 0.05, H0 should be kept. 
#That is, the difference in word length between fiction and non-fiction is not significant.

