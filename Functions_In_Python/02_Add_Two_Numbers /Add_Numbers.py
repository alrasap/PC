#-----------------------------------------------------------------------------
# Name:        Add Two Numbers (Add_Numbers.py)
# Purpose:     To demonstrate how to use a simple function in Python
#              that takes two numbers as input and returns their sum.
#
# Author:      Rohan
# Created:     Apr 29, 2025
# Updated:     Apr 29, 2025
#-----------------------------------------------------------------------------

# This function is called add_numbers.
# It takes two numbers as input (num1 and num2) and returns their sum.
def add_numbers(num1, num2):
    result = num1 + num2  # Add the two numbers
    return result  # Send the result back to where the function was called

# This loop allows the user to use the function again and again
while True:
    print("\nWelcome to the Add Two Numbers Program!")

    # Ask the user for the first number
    try:
        number1 = float(input("Enter the first number: "))
    except ValueError:
        print("That wasn't a number. Please try again.")
        continue

    # Ask the user for the second number
    try:
        number2 = float(input("Enter the second number: "))
    except ValueError:
        print("That wasn't a number. Please try again.")
        continue

    # Call the function and store the result
    total = add_numbers(number1, number2)

    # Show the result to the user
    print(f"The sum of {number1} and {number2} is {total}.")

    # Ask the user if they want to continue
    again = input("Would you like to add more numbers? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thank you for using the program. Goodbye! 👋")
        break
