#program created using dictionary and made mini grocery store.

print("-----The Fruit Land-----")
item_price={"apple":50,"mango":100,"watermelon":80,"kiwi":250,"guava":30,"avocado":500}         #used dictionary to store item and price
item=input("Enter fruit name: ")
quantity=int(input("Enter quantity of fruits: "))       #takes input from user for item and quantity
if item in item_price:
    print(item_price[item]*quantity,"Total price")      #calculates total price for the item
else:
    print("Not available in store!!!")      #if item not found in dictionary it shows not available message 