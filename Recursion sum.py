#program made by function recursion

def sum(n):
    '''Takes the input from the user and prints the sum of N natural numbers'''     #docstring
    if(n==0):
        return 0
    else:
        return n+sum(n-1)               #recursive call
n1=int(input("Enter any value: "))
print(sum(n1))
print(sum.__doc__)                #printing docstring   