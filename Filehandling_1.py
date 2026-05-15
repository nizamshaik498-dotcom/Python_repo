#Created a program to perform file handling operations on it

with open ("notes.txt","w") as file:
    file.write("Used writing method here")

with open ("notes.txt","r") as file:
    print(file.read())

with open("notes.txt","a") as file:
    file.write("\nUsed append method here")

with open("notes.txt","r") as file:
    print(file.read())


with open("notes.txt","r") as file:
    for line in file:
        print(line)


new=input("Enter  any info: ")
with open("notes.txt","a") as file:
    file.write(new)

with open ("notes.txt","r") as file:
    print(file.read())

with open ("notes.txt","r") as file:
    print(file.readline())

with open ("notes.txt","r") as file:
    print(file.readlines())