# -----------------------------------------------------------------------------
# Name:        Creating Sets
# Purpose:     To demonstrate how to create and print sets in Python.
#              The program shows how to define a set with unique elements
#              and then prints the set.
#
# Author:      Rohan
# Created:     02-April-2025
# Updated:     02-April-2025
# -----------------------------------------------------------------------------

# Step 1: Define a set called 'fruits' with the following items:
fruits = {'apple', 'banana', 'cherry'}

# Step 2: Print the 'fruits' set to see its contents.
print(fruits)

# Step 3: Ask the user if they want to create and print another set
while True:
    user_input = input("Would you like to create and print another set? (yes/no): ").strip().lower()

    if user_input == 'yes':
        # If the user says yes, we repeat the process.
        fruits = {'orange', 'grape', 'kiwi'}
        print(fruits)
    elif user_input == 'no':
        print("Thank you for using the Set Creator program!")
        break
    else:
        print("Invalid input! Please enter 'yes' or 'no'.")
