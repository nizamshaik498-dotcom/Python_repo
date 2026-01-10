#Program created using enumarate function which shows both index number and value stored in the list

Fruits=["Apple","Mango","Guava","Pine apple","Orange","Melon","Kiwi"]               #used an list of fruits
for index,value in enumerate(Fruits ,start=1):                                      #prints index number starting from 1
    print(index,value)
#  Another way to write the same code
print("Another way to write the same code")
for index,value in enumerate(Fruits):                                               #prints index number starting from 0
    print(index,value)
