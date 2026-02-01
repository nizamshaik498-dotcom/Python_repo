#program created using list and for loop with if else statements

nums=list(map(int,input("Enter numbers: ").split()))
even=0
odd=0
for num in nums:
    if num%2==0:
        even+=1
    else:
        odd+=1
print("Even Numbers: ",even)
print("Odd Numbers: ",odd)