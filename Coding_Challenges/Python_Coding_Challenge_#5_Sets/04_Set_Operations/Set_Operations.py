# -----------------------------------------------------------------------------
# Name:        Set Operations (Set_Operations.py)
# Purpose:     To demonstrate basic set operations such as union, intersection,
#              and difference in Python.
#              This program helps users understand how to manipulate sets using
#              these fundamental operations.
#
# Author:      Rohan
# Created:     04-Apr-2025
# Updated:     04-Apr-2025
# -----------------------------------------------------------------------------
# This program showcases set operations in Python:
# 1. Union: Combines all elements from two sets.
# 2. Intersection: Finds elements that are present in both sets.
# 3. Difference: Identifies elements in the first set that are not in the second set.
#
# After performing the operations, the program allows the user to choose if they
# want to perform another operation or exit.

def display_operations():
    # Display the results of set operations
    print("\n--- Results of Set Operations ---")
    print(f"Union: {union_result}")
    print(f"Intersection: {intersection_result}")
    print(f"Difference: {difference_result}")


# Define two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Perform union operation
union_result = set1 | set2

# Perform intersection operation
intersection_result = set1 & set2

# Perform difference operation
difference_result = set1 - set2

# Display the results
display_operations()

# Ask the user if they want to perform another set operation
while True:
    user_choice = input("\nWould you like to perform another set operation? (yes/no): ").strip().lower()

    if user_choice == "yes":
        print("\nLet's perform more set operations!")

        # Redefine sets for demonstration
        set1 = {1, 2, 3, 4}
        set2 = {3, 4, 5, 6}

        # Perform operations again
        union_result = set1 | set2
        intersection_result = set1 & set2
        difference_result = set1 - set2

        # Display updated results
        display_operations()

    elif user_choice == "no":
        print("\nThank you for using the Set Operations program. Goodbye!")
        break
    else:
        print("\nInvalid input. Please type 'yes' to continue or 'no' to exit.")
