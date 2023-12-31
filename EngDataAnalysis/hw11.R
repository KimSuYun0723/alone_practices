library(tokenizers); library(tidytext); library(dplyr); library(moments)
library(ggplot2); library(wordcloud2); library(readr); library(tidyverse)
library(viridis)

speech_of <- function (name, cutoff){
  sou <- subset(sou, sou$president == name) #subseting relevant data texts
  sou <- sou %>% unnest_tokens(word, text)
  sou <- data.frame(sou)
  sou <- sou %>% count(word, sort =TRUE) #counting word frequency
  sou <- sou %>% anti_join(stop_words) #removing stopwords
  df.sou <- sou[sou$n>cutoff,] #cutting off less frequent words
  mfrow = c(2,1)
  #drawing word charts
  ggplot(df.sou, aes(x=reorder(word,n), y=n)) +geom_col() +coord_flip() +ggtitle("Specific President's Speech Frequency")
  #wordclouds
  wordcloud2(data=df.sou)
}

speech_of("George Washington", 30)
