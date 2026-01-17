#program created using while loop,if, elif, else statements (Phone Lock).

password=4321
attempts=3                                     #setting number of attempts

while attempts>0:                                       #used while loop to allow multiple attempts
    pin=int(input("Enter PIN Number: "))
    if pin==password:                                   #used if block to check if the entered pin is correct
        print("Phone Unlocked")
        break
    else:
        attempts= attempts-1                            #decrementing attempts if the pin is wrong
        print("Wrong PIN!")
        print("Attempts Remaining: ",attempts)
    if attempts==0:                                      #used if block to check if attempts are over
        print("Phone Locked!!!")