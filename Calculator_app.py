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
        raise ValueError("\033[1;31;40mInvalid operator\033[0m")
# Use def function to get user input 
# Display the options
# Get user input for the chosen operation
# An error  message will apper if the user enters an invalid choice
# Ask the user to input two numbers to perform the operation
# An error message will appear if the user enter invalid number then ask to enter their choice again
# Perform the selected operation
# Print the result