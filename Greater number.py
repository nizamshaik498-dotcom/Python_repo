#program that shows which number is greater by seeing theinput given by the user 

A=int(input("Enter first value: "))
B=int(input("Enter second value: "))
if A>B:
    print(A,"Greater than B value")
if A==B:
    print(A,B,"Both are same values")
elif B>=A:
    print(B,"Greater than A value")

#can be used to compare marks between two students