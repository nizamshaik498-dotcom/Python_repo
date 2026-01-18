#program created using if, else, while loop (user need to find the special number and if its found he wins or he losses).

num=7
attempts=3
while attempts>0:
    value=int(input("Enter the special number: "))
    if value==7:
        print("You found the special number🥳")
        break
    else:
        attempts=attempts-1
        print("Ahh its not special🥺")
        print("Attempts Left: ",attempts)
        if attempts==0:
            print("Game Over❌❌")



            