# Created a program which takes input from user and checks if user is available or not

username=input("Enter username: ")
password=input("Enter passsword: ")
Users={"alex":"1234","charlie":"2431"}
def login(username,password):
    print(username,password)
    if username in Users:
        if Users[username]==password:
            print("Login Sucessful")
        else:
            print("Wrong Password")
    else:
        print("User not found")
login(username,password)