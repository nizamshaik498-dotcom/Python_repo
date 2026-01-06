#program created by using exception handling statements like (try,except)

try:                                                    #used try  block
    a=int(input("Enter 1st value: "))
    b=int(input("Enter 2nd value: "))
    print(a/b)
except ZeroDivisionError:                                  #used except block
    print("Cannot divide by zero")
except ValueError:
    print("invalid input")
else:                                                       #used else block
    print("Answer:",a/b)