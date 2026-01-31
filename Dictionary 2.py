#program created using dictionary to store contacts
name=input("Enter name: ")                                                          #input name to search in contacts
contacts={"nizam":154251,"althaf":567423,"wahid":654786,"mike":367399}              #dictionary to store contacts
name=name.lower()                                                                   #convert input name to lowercase    
if name in contacts:
    print("The mobile number is: ",contacts[name])
else:
    print("Person not found")