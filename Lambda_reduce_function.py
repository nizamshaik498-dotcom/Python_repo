#Created a program using lambda reduce function to find out the largest number.
from functools import reduce
nums=[10,50,20,90,30]
result=reduce(lambda a,b: a if a>b else b,nums)
print(result)