#program created using if, else statements and by using arthimetic operators(generates discount while purchase is more than 1000 rupees).

name=input("Enter your name: ")                             #taking user input
product=input("Enter product name: ")
price=int(input("Enter the price: "))
quantity=int(input("Enter the quantity: "))
total=price*quantity                                        #calculating total amount

if price>=1000:
    print("Total amount: ",price*quantity)                  #displaying total amount
    print("Discount applied🥳: ",price*quantity/10)        #displays the discount applied
    print("Final amount: ",price*quantity-price/10)         #displays the final amount after discount
    print(f"Thank you {name} for shopping with us😍!")          #displays thank you message
else:
    print(product,price,"No discounts applied❌")           #displays no discount applied message

