#Created a program using lambda filter function to find out the odd numbers only.

nums=[1,2,3,4,5,6,7,8,9]
result=list(filter(lambda n:n%2==1,nums))
print(result)