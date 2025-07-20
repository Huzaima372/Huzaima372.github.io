"""
Create a calculator program using a Python function named calculate(a, b, operation) that performs basic arithmetic operations. The user should enter two numbers and an operator as input. Based on the operator, the function should perform one of the following:
Addition (add)
Subtraction (sub)
Multiplication (multiply)
Division (divide)
Make sure to:
Convert user inputs to numbers (e.g., float)
Check for division by zero
Handle invalid operators gracefully
"""

def calculate(a, b, operation):
    if operation == 'sub':
        ans = a - b
    elif operation == 'add':
        ans = a + b
    elif operation == 'multiply':
        ans = a * b
    elif operation == 'divide':
        if b != 0:
            ans = a / b
        else:
            print("Cannot divide by zero.")
            return
    else:
        print("Invalid operator")
        return

    print("Result:", ans)

# Take input from the user
a = float(input("Enter num1: "))
operation = input("Enter an operator (add, sub, multiply, divide): ").strip().lower()
b = float(input("Enter num2: "))

# Call the function
calculate(a, b, operation)
