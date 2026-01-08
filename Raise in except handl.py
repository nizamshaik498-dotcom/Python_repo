#program made using exception handling statements and using (raise) and raising an eception

try:                                                                #used try block to check for exception
    num=int(input("Enter any value: "))
    if num<=0:                                                      #used if statement to check condition
        raise ValueError("Enter value greater than zero")
    print(num**2)                                                   #used raise statement to raise an exception
except ValueError as e:                                             #used except block to handle the exception
    print("Error: ",e)