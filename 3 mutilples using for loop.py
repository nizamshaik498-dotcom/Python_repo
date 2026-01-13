#program made using for loop which prints the 3 multiples from the values which are in the list.

num=[3,6,9,12,15]
for mul in num:
    if mul %3==0:
        print(mul,"is a multiple of 3")
    else:
        print("Not multiple of 3")