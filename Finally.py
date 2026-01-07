#program made by using exception handling statements and using (finally) block in it

print("A mini calculator which performs division operation:")

try:                                                        #used try block to take input from user
    num1=int(input("Enter first value: "))
    num2=int(input("Enter second value: "))
    result=(num1/num2)
    print("Your answer is:",result)                        #only this line will execute if there is no exception
except ZeroDivisionError:                                  #used except block to handle the exception   
    print("Sorry! cant divide with zero")
except ValueError:                                         #used another except block to handle another exception
    print("please enter value in integer type")
finally:                                                   #used finally block to execute the code at last
    print("Thank you for using this mini divisable calculator")
    



