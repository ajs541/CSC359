print("hello world")
print(5 + 5)
#plot(1:10)
for (x in 1:10) {
  print(x)
}
y <- 3.14
print(class(y))
str <- "This is a multi
line string tester thing,
hello world"
print(cat(str))
str2 <- "test"
str3 <- paste(cat(str), str2)
print(str3)
str4 <- "Testing out \'illegal\' characters"
print(cat(str4))

tester <- 1
while (tester < 10){
  print(tester)
  tester <- tester + 1
}
#vectors are collections of components. (same type)
vector <- c(TRUE, TRUE, FALSE)
vector2 <- c(FALSE, TRUE, TRUE)
vector3 <- 1:5
odds <- seq(1, 11, 2)
#R indexing starts at 1!!!
print(vector3)
print(odds)
my_name <- c(fname = "Aaron", lname = "Standefer")
print(names(my_name))
print(is.character(my_name))
x <- 1:3
y <- 4:6
z <- cbind(x, y)
z1 <- rbind(x, y)
print(z)
print(z1)
z2 <- matrix(1:10, nrow = 5)
print(z2)
colnames(z2) <- c("x", "y")
print(z2)
#Data Frame: tables
#Collections of vectors, all vectors have same length
num <- 1:3
let <- c("a", "b", "c")
TorF <- c(TRUE, F, T)
df <- data.frame(num, let, TorF)
print(df)
print(df$let)
print(df[, "let"])
print(df[, 2])
#loops are inefficient in R!!!
my_function <- function(var1, var2){
  return(var1 + var2)
}
print(my_function(55, 30))
#R has other methods that can do similar things faster!!!
nums <- 1:5
print(nums**2)

i <- 0
while(i**2 < 100){
  print(i)
  i <- i + 1
}