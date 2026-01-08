#program made using exception handling statements and using (raise) and raising an eception

try:
    num=int(input("Enter any value: "))
    if num<=0:
        raise ValueError("Enter value greater than zero")
    print(num**2)
except ValueError as e:
    print("Error: ",e)