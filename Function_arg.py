#Created a program usinf function arguements using (*arg).

def multiply(*numbers):
    total=1
    for i in numbers:
        total *= i
    print(total)
multiply(2,3,4)