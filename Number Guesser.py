#program created using loop and if else contition for making (number guessing game).

num=57                                                                      
attempts=5                                                                      #assigning the number of attempts and the number to be guessed.

while attempts>0:                                                               #using while loop to check the number of attempts and to take input from user until the attempts are over or the user wins.
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
