#program created by using if, elif, else statements (generates exam results ).

print("----------Board Exams Result Generator----------")
name=input("Enter your name: ")
m1=int(input("Enter 1st subject marks: "))
m2=int(input("Enter 2nd subject marks: "))
m3=int(input("Enter 3rd subject marks: "))
total=m1+m2+m3
average=total/3
total1=print("Your total: ",total)
average1=print("Average: ",average)
if average<=0:
    print("F-grade")
    print(f"{name},you failed")
elif average<=35:
    print("C-grade")
    print(f"{name},you just passed!!!")
elif average>35 and average<=50:
     print("B-grade")
     print(f"{name},Good Keep Going")
elif average>50 and average<=80:
    print("A-grade")
    print(f"{name},Superb Keep it up")
else:
    print("A+ grade")
    print(f"{name},Congratulations topper of board exams")