#program to take input from the user and tell whether it is positive,negative or zero(null)

value=int(input("Enter any value: "))
print("Your entered value is:",value)
if value >0:
    print(value,"is positive number")
if value <0:
    print(value,"is negative number")
if value==0:
    print(value,"is null value")