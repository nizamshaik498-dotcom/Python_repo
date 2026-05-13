#Created a recursive function program which prints numbers in reverse order

def fun1(n):
    if n==0:
        return
    print(n)
    fun1(n-1)
fun1(5)