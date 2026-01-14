#Program created using list and for loop as well as if, else statement

nums=[1,2,3,4,5,6,7,8,9,10]
Even_count=0
Odd_count=0
for n in nums:
    if n%2==0:
        Even_count +=1
    else:
        Odd_count +=1
print("Even count: ",Even_count)
print("Odd_count: ",Odd_count)
