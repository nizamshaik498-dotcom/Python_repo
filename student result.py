#program that shows whether the student is pass or fail by taking input from user,by using if,else and elif coditions

Marks=int(input("Enter your marks: "))
if Marks <=35:
    print(Marks,"You failed") 
elif Marks >35 and Marks <=50:
    print(Marks,"B")
elif Marks >50 and Marks <=80:
    print(Marks,"A")
else:
    print(Marks,"A+")