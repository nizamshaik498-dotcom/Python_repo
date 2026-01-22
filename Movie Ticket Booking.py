#program created using if, elif, else statements and by using arthimetic operators.

name=input("Enter your name: ")
age=int(input("Enter your age: "))
tickets=int(input("Enter number of tickets: "))

if age<12:
    price_per_ticket=100
elif age<=60:
    price_per_ticket=200
else:
    price_per_ticket=150

total_amount=price_per_ticket*tickets                     #calculating total amount

if tickets>5:
    discount=total_amount*0.10
else:
    dicount=0

final_amount=total_amount-discount                       #calculating final amount after discount                       

print("-----Movie Ticket Bill-----")                            #whole bill generation
print("Customer Name: ",name)
print("Ticket Price: ",price_per_ticket)
print("Number Of tickets: ",tickets)
print("total Amount: ",total_amount)
print("Discount: ",discount)
print("Final Amount To Pay: ",final_amount)
print("-----------------------------")