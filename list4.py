#program created using list which stores the values given by user in it and shows largest, smallest and average of the values

num=list(map(int,input("Enter numbers: ").split())) #takes input from user and store in the list
largest=max(num)                                    #finds the largest number in the list
smallest=min(num)                                   #finds the smallest number in the list
average=sum(num)/len(num)                           #finds the average of the numbers in the list
print("The largest number is: ",largest)
print("The smallest number is: ",smallest)
print("The average is : ",average)