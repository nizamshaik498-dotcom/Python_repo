#program to check whether the person is child,teenager,adult or old by taking input from the user

age=int(input("Enter your age:"))
print("Your age is",age)
if age >0 and age <=10:
    print(age,"you are a child")
if age >10 and age <=18:
    print(age,"you are a teenager")
if age >18 and age <=50:
    print(age,"you are a adult")
if age >50:
    print(age,"you are old")
