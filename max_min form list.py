#Created a program which takes input from user into a list and then returns it max and min elements

L=[]
l1=int(input("Enter how many elements want: "))
for i in range(l1):
    l2=int(input("Enter the element values: ".format(i+1)))
    L.append(l2)
print(L)
print(max(L))
print(min(L))





