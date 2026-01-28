#program created using string methods .(character frequency counter).

query=input("Enter any sentence: ")         #takes input from user
lower=0
upper=0
digit=0
space=0
for n in query:
    if n.islower():
        lower+=1
    elif n.isupper():
        upper+=1
    elif n.isdigit():
        digit+=1
    elif n.isspace():
        space+=1
    print("Lowercase Letters: ",lower)
    print("Uppercase letters: ",upper)
    print("Digits: ",digit)
    print("Spaces: ",space)

