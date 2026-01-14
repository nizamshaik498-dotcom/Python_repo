#Program made using if, else conditions and by using comparision (==) operator
name="Nizam"
password=154251
User_name=input("Enter your name: ")
User_password=int(input("Enter your password: "))
if User_name==name and User_password==password:
    print("Access granted")
else:
    print("Access Denied")