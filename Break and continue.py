#program using break and continue statements and while loop in it 
while True:
    i=int(input("Enter any num:"))
    if i<0:
        print("skipped negative value")
        continue        #used continue here to skip
    elif i==0:
        print("stopped loop you entered zero")
        break           #used break here to stoop the loop
    else:
        print(i,"Entered positive number")    
