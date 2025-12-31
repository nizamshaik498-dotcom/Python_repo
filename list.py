#program using list and asking user to input values in the empty list and using loop 

Numbers=[]
n=int(input("Enter the number of elements you want to add to the list: "))
for i in range(n):
    element=int(input("Enter element {}: ".format(i+1)))
    Numbers.append(element)
print("The complete list is:", Numbers)
print("The length of the list is:", len(Numbers))
print("The sum of the list elements is:", sum(Numbers))

