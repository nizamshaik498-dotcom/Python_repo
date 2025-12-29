#program using for loop and strings by taking input from user and printing each character in new line and also checking its length without using len() function.
Input=input("Enter string value:")
count=0
for i in Input:
    print(i)
    count=count+1  #This tells the length of string without using len() function
print("Length of string is:",count)
