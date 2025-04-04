# -----------------------------------------------------------------------------
# Name:        Sets vs Lists (sets_vs_lists.py)
# Purpose:     To compare the behavior of lists and sets in Python.
#              The program demonstrates how lists can contain duplicate values,
#              while sets automatically remove duplicates.
#
# Author:      Rohan
# Created:     4-April-2025
# Updated:     4-April-2025
# -----------------------------------------------------------------------------

# Create a list with some numbers, including duplicates
num_list = [1, 2, 2, 3, 4, 4, 5]

# Print the original list with duplicates
print("Original List (with duplicates):", num_list)

# Convert the list into a set to automatically remove duplicates
num_set = set(num_list)

# Print the set after conversion, which will not have duplicates
print("Converted Set (duplicates removed):", num_set)

# Ask the user if they want to try with a different list or exit
while True:
    # Give the user an option to continue or exit
    user_input = input("\nWould you like to try again with a different list? (yes/no): ").strip().lower()

    if user_input == 'yes':
        # Ask the user to input a new list of numbers separated by commas
        new_list = input("Enter a new list of numbers, separated by commas (e.g., 1, 2, 2, 3): ")
        # Convert the input string into a list of integers
        num_list = [int(x) for x in new_list.split(',')]

        # Show the original list and its set conversion
        print("\nOriginal List (with duplicates):", num_list)
        num_set = set(num_list)
        print("Converted Set (duplicates removed):", num_set)

    elif user_input == 'no':
        print("Thank you for using the program!")
        break  # Exit the loop if the user doesn't want to try again

    else:
        # If the user enters something other than 'yes' or 'no', prompt again
        print("Please enter 'yes' or 'no'.")
