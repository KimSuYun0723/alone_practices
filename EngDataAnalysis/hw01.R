#first function
m2k <- function(mile){
  kilo <- 1.6*mile
  cat(kilo, "km")
}


#second function
inch2cm <- function(inch){
  cm <- 2.54*inch
  cat(cm, "cm")
}


#third function
even_odd <- function(num){
  if (num%%2 == 0){
    print("Even")
  } else if (num%%2 == 1) {
    print("Odd")
  } else {
    print("Something is wrong")
  }
}


#fourth function
i_feel <- function(day){
  if (day == "Monday"){
    print("I am tired")
  } else if (day == "Saturday"){
    print("I am happy")
  } else if (day == "Wednesday"){
    print("I am dying")
  } else {
    print("It will pass")
  }
}
