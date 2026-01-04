#program made by using list 
id_list={101,102,103,104}
id_no=int(input("Enter your id number: "))
if (id_no in id_list):                          #used in operator to check whether the id number is present in the set or not
    print("Access Granted")
else:
    print("Access denied")
