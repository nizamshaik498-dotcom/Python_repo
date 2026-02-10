#program created using (oop) based for bank.

class BankAccount:                                                      #bank account class created
    def __init__(self,acname,acnum,balance):                            #constructor created to initialize the attributes of the class
        self.acname=acname
        self.acnum=acnum
        self.balance=balance
    def display(self):                                                  #method created to display the account details
        print("account holder name: ",self.acname)
        print("account number: ",self.acnum)
        print("account balance: ",self.balance)
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Amount Deposited: ",amount)
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            print("Amount Withdrawn: ",amount)
        else:
            print("Insufficient Balance")
d=BankAccount("Alex",501250,50000)
d.deposit(5000)
d.withdraw(12000)
d.display()