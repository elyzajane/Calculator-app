#Elyza Jane G. Relucio 
#BSCPE 1-4

# Display a greeting message for the user
print("\033[1;35;40m╦ ╦ ╦═╗╦  ╦  ╔═╗")
print("\033[1;35;40m╠═╣ ╠═ ║  ║  ║ ║")
print("\033[1;35;40m╩ ╩ ╩═╝╩═╝╩═╝╚═╝")

# Display a message reminding the user to use the calculator app wisely
print("\033[1;31;40mKindly use the calculator app wisely!\033[0m")

import operator

# Use def function to perform mathematical operations
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
def calculate():
# Display the options
    print("\033[1;33;40mPlease choose the operation.\033[0m")
    print("\033[1;32;40m1. Addition\033[0m")
    print("\033[1;36;40m2. Subtraction\033[0m")
    print("\033[1;34;40m3. Multiplication\033[0m")
    print("\033[1;35;40m4. Division\033[0m")

# Get user input for the chosen operation
    while True:
        try:
            operation = int(input("Enter your choice (1/2/3/4):"))
# An error  message will apper if the user enters an invalid choice
            if operation < 1 or operation > 4:
                raise ValueError
            break
        except ValueError:
            print("A! Please enter a valid choice.")
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
    print((num1, operator_symbol, num2, result))

     # Ask the user if they want to perform another calculation with the given choices (yes or no)
    while True:
        try:
            choice = input("Do you want to perform another calculation? (yes/no):")
            if choice.lower() == 'yes':
                calculate()
                break
            elif choice.lower() == 'no':
                print("Thank you and have a good day!")
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid input! Please enter 'yes' or 'no'")
        calculate()
        return
    # Use the calculate function to start the program
calculate()

