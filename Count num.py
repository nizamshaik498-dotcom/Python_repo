#Program created using list and for loop as well as if, else statement

nums=[1,2,3,4,5,6,7,8,9,10]             #list of numbers from 1 to 10
Even_count=0                            #used even count variable to count even numbers
Odd_count=0                             #used odd count variable to count odd numbers
for n in nums:
    if n%2==0:
        Even_count +=1                  #incrementing even count by 1
    else:
        Odd_count +=1                   #incrementing odd count by 1
print("Even count: ",Even_count)
print("Odd_count: ",Odd_count)
