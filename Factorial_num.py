#program created by using recursion and docstring to calculate factorial of an number

def factorial(n):
    ''' Takes an input value from the user and prints its factorial'''      #docstring
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)         #recursive call
n1=int(input("enter any value: "))
print(factorial(n1))
print(factorial.__doc__)                #printing docstring

