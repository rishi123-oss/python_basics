def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b==0:
        print("Error: denominator can't be 0")
    return a/b

def calculator():
    print("Simple Calculator")  
    print("Operations: +, -, *, /")

while True:
    num1 = float(input("Enter the 1st number: "))
    operator = input("Enter the operator (+,-,*,/): ")
    num2 = float(input("Enter the secod number: "))

    if operator == "+":
        result = add(num1,num2) 
    elif operator == "-":
        result = subtract(num1,num2)
    elif operator == "*":
        result = multiply(num1,num2)
    elif operator == "/":
        result = divide(num1,num2)
    else:
        print("Invalid operator. Try again.")
        continue

    print(f"Result: {num1} {operator} {num2} = {result}")

    again = input("Calculate again? (yes/no):").lower() 
    if again != "yes":
        break 

calculator() 