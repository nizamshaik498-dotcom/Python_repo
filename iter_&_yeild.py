#Created a program using iter and yield(generators).

def countdown():
    yield 5
    yield 4
    yield 3
    yield 2
    yield 1
x=countdown()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))