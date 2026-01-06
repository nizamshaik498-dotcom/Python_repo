#program created by using exception handling statements like (try,except)

try:
    a=int(input("Enter 1st value: "))
    b=int(input("Enter 2nd value: "))
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("invalid input")
else:
    print("Answer:",a/b)