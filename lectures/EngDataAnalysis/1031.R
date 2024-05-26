ldt <- read.csv((file.choose()))
head(ldt)

a <- order(ldt$Length);a #order, sort
b <- sort(ldt$Length);b
a[50:51]
b[50:51]


typeof(1:7)

a <- c(TRUE, FALSE, 0,1, "1")
class(a)
