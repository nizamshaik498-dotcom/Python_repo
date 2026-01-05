#program created by using dictionary and asks the user to enter product name if avilable then printd them else prints not available

print("WELCOME  TO  MY  STORE")
products={"Shirts":500,
          "Pants":700,
          "Perfumes":850,
          "Wallet":500,
          "Shoes":1200,
          "Belts":600,
          }
product=(input("Enter product name: "))
if product in products:
    print(products[product],"Available in store")
else:
    print("Product not available")

