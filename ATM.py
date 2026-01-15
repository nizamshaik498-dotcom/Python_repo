#program created using if, else and elif conditions . (ATM mini system)

pin=1234
balance=5000

atm_pin=int(input("Enter ATM pin: "))                           #takes input from user
if atm_pin!=pin:
    print("Incorrect PIN")
else:
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Exit")

    choice=int(input("Choose any option: "))                    #takes input from user
    if choice==1:
        print("Your available balance: ",balance)
    elif choice==2:
        amount=int(input("Enter Amount: "))
        if amount>balance:
            print("Insufficient Balance")
        else:
            balance=balance-amount
            print("Remaining balance: ",balance)
    elif choice==3:
        print("Thank you, visit again")
    else:

        print("Invalid choice")    