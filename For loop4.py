#program created using for loop which prints number which are greater and less than 10.

num=[2,5,8,11,14]
for value in num:                               #used for loop to iterate through the list
    if value>10:                                #used if else condition to check whether the number is greater than 10 or not
        print(value,"is greater than 10")
    else:
        print(value,"not greater than 10")