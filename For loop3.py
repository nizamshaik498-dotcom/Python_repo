#Program using for loop which prints only even numbers from the values which are stored in the list

num=[1,2,3,4,5]
for even in num:
    if even %2==0:                                  #used if condition to check even numbers
        print("These are even num:",even)
        

#program using for loop which prints only odd numbers from the values which are stored in the list
num=[1,2,3,4,5]
for odd in num:
    if odd %2!=0:
        print("These are odd num:",odd)