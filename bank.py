
balance=50000

def bank():
    global balance
    while True:

        print("1.Show balance")
        print("2.Deposit amount")
        print("3.Withdraw amount")
        print("4.Exit")

        try:
            choice=int(input("Choose any option: "))
            if choice==1:
                print("Current Balance: ",balance)
            elif choice==2:
                amount=int(input("Enter amount to deposit: "))
                balance+=amount
                print("Updated Balance: ",balance)
            elif choice==3:
                amount=int(input("Enter amount to withdraw: "))
                if amount>balance:
                    print("Insufficient Balance")
                else:
                    balance-=amount
                    print("Updated Balance: ",balance)
            elif choice==4:
                print("Thank you for using our service")
                break
            else:
                print("Enter valid choice among 4 options")
        except ValueError:
            print("Please enter valid input")
bank()
    