#Elyza Jane G. Relucio 
#BSCPE 1-4

# A program that allows you to perform basic mathematical operations on two numbers. The program will then display the result and ask if you want to try again.

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
            operation = int(input("\033[1;33;40mEnter your chosen operation (1/2/3/4): \033[0m"))
# An error  message will apper if the user enters an invalid choice
            if operation < 1 or operation > 4:
                raise ValueError
            break
        except ValueError:
            print("\033[1;31;40mAn error occured! Please enter a valid choice (1/2/3/4).\033[0m")
# Ask the user to input two numbers to perform the operation
    while True:
        try:
            num1 = float(input("\033[1;33;40mEnter first number: \033[0m"))
            num2 = float(input("\033[1;33;40mEnter second number: \033[0m"))
            break
        except ValueError:
# An error message will appear if the user enter invalid number then ask to enter their choice again
            print("\033[1;31;40mAn error occured! Please enter a valid numbers.\033[0m")
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
    print("\033[1;34;40m{} {} {} = {}\033[0m".format(num1, operator_symbol, num2, result))

     # Ask the user if they want to perform another calculation with the given choices (yes or no)
    while True:
        try:
            choice = input("\033[1;33;40mDo you want to perform another calculation? (yes/no): \033[0m")
            if choice.lower() == 'yes':
                calculate()
                break
            elif choice.lower() == 'no':
                print("\033[1;31;40mThank you and have a good day!\033[0m")
                break
            else:
                raise ValueError
        except ValueError:
            print("\033[1;31;40mAn error occured! Please enter 'yes' or 'no'.\033[0m")
        calculate()
        return
    # Use the calculate function to start the program
calculate()

