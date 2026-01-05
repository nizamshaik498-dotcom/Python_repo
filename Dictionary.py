#program created by using dictonary and printing the sum and average of the values in the dictionary present

Marks={"English":95,                #dictionary stored with values with its items
       "Sanskrit":92,
       "Maths":90,
       "Physics":72,
       "Computers":89}
print(Marks["English"])
print(Marks["Sanskrit"])
print(Marks["Maths"])
print(Marks["Physics"])
print(Marks["Computers"])

add=(95+92+90+72+89)                #Sum the total marks
print("Total Marks: ",add)
avg=(95+92+90+72+89/5)              #Average of the marks
print("Average: ",avg)

print(type(Marks))                  #prints the type of the variable Marks

