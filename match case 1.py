#program on making a calculator using matchcase

value=int(input("Enter first number: "))
value2=int(input("Enter second number: "))
operation=input("Enter operation (+, -, *, /): ")   
match operation:
    case "+":
        print(f"The sum is: {value + value2}")
    case "-":
        print(f"The difference is: {value - value2}")
    case "*":
        print(f"The product is: {value * value2}")
    case "/":
        if value2 != 0:
            print(f"The quotient is: {value / value2}")
        else:
            print("Error: Division by zero is not allowed.") 