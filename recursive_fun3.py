#Created an recxursive function program which finds out the squares of numbers given 

def sqr(n,a):
    if a==0:
        return 1
    return n*sqr(n,a-1)
print(sqr(2,4))