#program created using while loop,if, elif, else statements (Phone Lock).

password=4321
attempts=3

while attempts>0:                                       #used while loop to allow multiple attempts
    pin=int(input("Enter PIN Number: "))
    if pin==password:                                   #used if block to check if the entered pin is correct
        print("Phone Unlocked")
        break
    else:
        attempts= attempts-1
        print("Wrong PIN!")
        print("Attempts Remaining: ",attempts)
    if attempts==0:
        print("Phone Locked!!!")