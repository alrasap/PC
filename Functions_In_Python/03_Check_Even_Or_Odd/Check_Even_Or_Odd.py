#-----------------------------------------------------------------------------
# Name:        Check Even or Odd (Check_Even_Or_Odd.py)
# Purpose:     To demonstrate how to write a function in Python that checks
#              whether a number is even or odd and returns True or False.
#
# Author:      Rohan
# Created:     Apr 30 2025
# Updated:     Apr 30 2025
#-----------------------------------------------------------------------------

# This function is called is_even.
# It takes one number as input and checks if it is even.
# If the number is even, it returns True. If it's odd, it returns False.
def is_even(number):
    return number % 2 == 0  # Even numbers have no remainder when divided by 2

# Keep asking the user to check numbers until they say they want to stop
while True:
    print("\nWelcome to the Even or Odd Checker!")

    # Ask the user for a number
    try:
        user_input = int(input("Enter a whole number to check: "))
    except ValueError:
        print("Oops! That wasn't a valid number. Please try again.")
        continue

    # Use the function to check if it's even or odd
    if is_even(user_input):
        print(f"{user_input} is EVEN.")
    else:
        print(f"{user_input} is ODD.")

    # Ask if they want to check another number
    again = input("Would you like to check another number? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thanks for using the checker! Goodbye! 👋")
        break
