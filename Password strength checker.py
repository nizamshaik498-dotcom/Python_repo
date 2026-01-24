#program created using if, else, elif and string operations which checks the password strength entered by the user.

key=input("Enter Password: ")
length=6
if len(key)<6:
    print("Weak Password")
elif key.isdigit():
    print("Password should contain numbers and as well as letters")
else:
    print("Strong Password")