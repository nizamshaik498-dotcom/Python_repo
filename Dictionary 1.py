#program created by using dictionary and asks the user to enter product name if avilable then printd them else prints not available

print("WELCOME  TO  MY  STORE")
products={"Shirts":500,
          "Pants":700,
          "Perfumes":850,                           #created dictionary and stored my own values
          "Wallet":500,
          "Shoes":1200,
          "Belts":600,
          }
product=(input("Enter product name: "))
if product in products:                                 #checks if the product is in the dictionary
    print(products[product],"Available in store")       #prints the price of the product if available
else:
    print("Product not available")                      #prints this is not available

