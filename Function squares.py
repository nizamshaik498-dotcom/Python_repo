#program created using functions and prints the square value from the numbers given as input from the user.

val1=int(input("Enter 1st number: ")) #input from user
val2=int(input("Enter 2nd number: ")) #input from user
def value():
    num=val1*val1+val2*val2
    return num
out=value()
print("Output: ",out) 