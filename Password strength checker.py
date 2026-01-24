#program created using if, else, elif and string operations which checks the password strength entered by the user.

key=input("Enter Password: ")                                           #takes password input in both numbers and letters
if len(key)<6:                                                          #checks the length of password
    print("Weak Password")
elif key.isdigit():
    print("Password should contain numbers and as well as letters")
else:
    print("Strong Password")