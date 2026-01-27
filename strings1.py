#program created using string methods and converts the user input to title case and counts how many vowels are in it.

prompt=input("Enter any sentence: ")
print("Your Input Is: ",prompt)
print("Coverted to title case: ",prompt.title())
vowels=(prompt.lower().count('a')+
        prompt.lower().count('e')+
        prompt.lower().count('i')+
        prompt.lower().count('o')+
        prompt.lower().count('u'))
print("Vowels Found: ",vowels)