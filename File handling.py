#program created using file handling functions

username=input("Enter username: ")

with open("users.txt","a") as file:
    file.write(username+"\n")
print("\n Saved usernames: ")
with open("users.txt","r") as file:
    print(file.read())
    