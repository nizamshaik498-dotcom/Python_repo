#program made by function recursion

def sum(n):
    '''Takes the input from the user and prints the sum of N natural numbers'''
    if(n==0):
        return 0
    else:
        return n+sum(n-1)
n1=int(input("Enter any value: "))
print(sum(n1))
print(sum.__doc__)