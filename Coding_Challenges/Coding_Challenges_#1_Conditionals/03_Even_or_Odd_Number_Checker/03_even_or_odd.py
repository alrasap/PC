# Even or Odd Number Checker
# Purpose: This Python program asks the user for a number and tells them if the number is even or odd.
# Made by: Rohan
# Student number: 931006
# Date: February 26, 2025
#
# The program will:
# 1. Ask the user to input a number.
# 2. Store that number in a variable.
# 3. Check whether the number is even or odd using conditional statements.
# 4. Print whether the number is "even" or "odd" based on the result of the check.

# Step 1: Ask the user to enter a number
# The input() function allows the user to enter a value. We convert it to an integer using int().
user_input = input("Enter a number: ")  # Prompting the user to enter a number

# Step 2: Store the number in a variable
# We store the user input as an integer in the variable 'number'.
number = int(user_input)  # Convert the input into an integer and store it

# Step 3: Use a conditional statement to check if the number is even or odd
# An even number is divisible by 2, so we use the modulus operator (%) to check.
if number % 2 == 0:  # If the remainder when divided by 2 is 0, the number is even
    # Step 4: If the number is even, print "The number is even."
    print("The number is even.")  # Output message for even numbers
else:  # If the number is not even, it must be odd
    # Step 5: If the number is odd, print "The number is odd."
    print("The number is odd.")  # Output message for odd numbers
