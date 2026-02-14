#program created for showing the use of list functions.

# 1 max() function.                                                             #max() function is used to find the maximum value from a list of values.
prices=[159.4,120,80,70]
new_price=max(prices)
print("Max price: ",new_price)


# 2 min() function.                                                         #min() function is used to find the minimum value from a list of values.    
prices=[159.4,120,80,70]
new_price=min(prices)
print("Min price: ",new_price)


# 3 len() function.                                                     #len() function is used to find the length of a list or the number of items in a list.
stock_1=[150.23]
stock_2=[75.4,86.4,90.15]
print("stock_1 length: ",len(stock_1))
print("stock_2 length: ",len(stock_2))


# 4 list() function.                                                        #list() function is used to convert a tuple into a list.                                    
tup1=(1,4,5)
new_list=list(tup1)
print(new_list)


# 5 range() function
mylist=range(11)
for list in mylist:
    print(list)