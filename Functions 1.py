#program using function that asks input from the user and prints the length and breadth of a rectangle and also use return in it and prints the result

def calculate_area():
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    return length, breadth

length, breadth = calculate_area()
print(f"The length of the rectangle is: {length}")          #shows the length
print(f"The breadth of the rectangle is: {breadth}")        #shows the breadth
print(f"The area of the rectangle is: {length * breadth}")  #shows the area
