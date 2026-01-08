#program made using exception handling statements and using (raise) and raising an eception

try:                                                                #used try block to check for exception
    num=int(input("Enter any value: "))
    if num<=0:                                                      #used if statement to check condition
        raise ValueError("Enter value greater than zero")
    print(num**2)                                                   #prints the square of the number
except ValueError as e:                                             #used except block to handle the exception
    print("Error: ",e)