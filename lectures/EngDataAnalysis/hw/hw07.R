#Download data: L2_rating.csv
l2 <- read.csv(file.choose())

#Analyze 5 raters’ scores and check how consistent their rating patterns are
  # Perform pairwise checking with correlation coefficients 
l <- list(l2$rater01,l2$rater02,l2$rater03,l2$rater04,l2$rater05); l
vec <- numeric(n)
num =1

for (i in l) {
  for (j in l) {
    vec[num] <- cor(i, j)
    num <- num+1
  }
}

mt <- matrix(
  vec, nrow=5, ncol=5, byrow=TRUE
)

dimnames(mt) <- list(
  c("rater01", "rater02", "rater03", "rater04", "rater05"), 
  c("rater01", "rater02", "rater03", "rater04", "rater05")
)
excluded <- c(max(mt));excluded
max_val <- max(mt[mt != 1]);max_val

  #Who is the most reliable rater? 
m <- numeric(nrow(mt))
for (i in 1:nrow(mt)) {
  m[i] <- mean(mt[,i])
}
mt2 <- data.frame(
  names = c("rater01", "rater02", "rater03", "rater04", "rater05"),
  means = m
)

cat("The best correlation coefficient(r) :", max(mt2$means))
cat("The person who has the max correlation :", mt2$names[which(mt2$means == max(mt2$means))])



