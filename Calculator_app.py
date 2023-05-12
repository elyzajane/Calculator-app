# Use def function to perform mathematical operations
import operator

def operate(num1, num2, op):
    # Use if-else statements to know which operation is needed
    if op == "+":
        return operator.add(num1, num2)
    elif op == "-":
        return operator.sub(num1, num2)
    elif op == "*":
        return operator.mul(num1, num2)
    elif op == "/":
        return operator.truediv(num1, num2)
    else:
        raise ValueError("Invalid operator")
# Use def function to get user input 
def calculate():
# Display the options
    print("Please choose the operation:")
    print("Addition")
    print("Subtraction")
    print("Multiplication")
    print("Division")

# Get user input for the chosen operation
    while True:
        try:
            operation = int(input("Enter your choice (1/2/3/4):"))
# An error  message will apper if the user enters an invalid choice
            if operation < 1 or operation > 4:
                raise ValueError
            break
        except ValueError:
            print("Invalid choice! Please enter a valid choice.")
# Ask the user to input two numbers to perform the operation
    while True:
        try:
            num1 = float(input("Enter first number:"))
            num2 = float(input("Enter second number:"))
            break
        except ValueError:
# An error message will appear if the user enter invalid number then ask to enter their choice again
            print("An error occured! Please enter valid numbers.")
# Perform the selected operation
    if operation == 1:
        result = operate(num1, num2, "+")
        operator_symbol = "+"
    elif operation == 2:
        result = operate(num1, num2, "-")
        operator_symbol = "-"
    elif operation == 3:
        result = operate(num1, num2, "*")
        operator_symbol = "*"
    else:
        result = operate(num1, num2, "/")
        operator_symbol = "/"
# Print the result