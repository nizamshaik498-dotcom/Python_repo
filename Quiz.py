#program created using if statements and ask the user to enter the answers for the questions.

score=0
ans1=input("Who Is The CEO Of Tesla/X/Spacex: ")    #asking user for input
ans2=input("What Is The Abbrevation Of CEO: ")
ans3=input("What Is Trade ?: ")
if ans1.lower()=="elon musk":
    score+=1
if ans2.lower()=="chief executive officer":
    score+=1
if ans3.lower()=="buying and selling":
    score+=1
print("Your score is : ",score)