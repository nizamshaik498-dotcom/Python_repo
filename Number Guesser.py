#program created using loop and if else contition for making (number guessing game).

num=57
attempts=5

while attempts>0:
    number=int(input("Enter any random number: "))
    if number==num:
        print("***You won***")
        break
    elif number>num:
        print("Too High")
    else:
        print("Too Low")
    attempts-=1
    print("Attempts remaining: ",attempts)
if attempts==0:
    print("Game Over")
