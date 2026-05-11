#Created an program using list and function (mini shopping cart)

cart=[]
ask=int(input("How many items you want to add ? : "))
def show_items(cart):
    for i in range(ask):
        ask1=input("Enter item names: ")
        cart.append(ask1)
    print("Items in cart :")
    for i in cart:
        print(i)
show_items(cart)