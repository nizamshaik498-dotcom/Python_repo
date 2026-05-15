#Created a program which handles exceptions

try:
    num1=int(input("Enter first number :"))
    num2=int(input("Enter seconnd number: "))
    print(num1/num2)
except ZeroDivisionError:
    print("Cant divide with zero")
except ValueError:
    print("Please enter valid value")
finally:
    print("Program completed sucessfully")