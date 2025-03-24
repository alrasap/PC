# -----------------------------------------------------------------------------
# Name:        Grocery List (01_grocery_list.py)
# Purpose:     To demonstrate how to create a list and add items to it
#              using Python's list functions while preventing duplicates.
#
# Author:      Rohan
# Created:     March 20, 2025
# Updated:     March 20, 2025
# -----------------------------------------------------------------------------

# This program demonstrates how to create a grocery list in Python.
# It starts with some initial items, then adds two more items, and finally
# prints the updated list to the screen.

# Step 1: Create an initial grocery list with some itemsd
grocery_list = ['apples', 'bread', 'milk', 'eggs']

# Step 2: Add two more items to the list
grocery_list.append('cheese')  # Adds 'cheese' to the list
grocery_list.append('tomatoes')  # Adds 'tomatoes' to the list

# Step 3: Print the updated grocery list and interact with the user
print("This is what you have right now in your grocery list:")
print(grocery_list)

# Step 4: Ask if the user wants to add more items
while True:
    continue_adding = input("Do you want to add more items to the list? (yes/no): ").strip().lower()

    # Check if the user wants to continue
    if continue_adding == 'yes':
        item = input(
            "What item would you like to add? ").strip().lower()  # Convert input to lowercase to prevent case sensitivity

        # Check if the item is already in the list
        if item in grocery_list:
            print(f"{item} is already in the list. Please add a different item.")
        else:
            grocery_list.append(item)
            print(f"{item} has been added to the list.")

        # Show the updated list
        print("Updated Grocery List:", grocery_list)

    elif continue_adding == 'no':
        # Ask if the user is done
        done = input("Is that all for now? (yes/no): ").strip().lower()

        if done == 'yes':
            print("Thank you for using the grocery list program!")
            break
        elif done == 'no':
            print("You can continue adding items at any time. Let's add more!")
        else:
            print("Invalid input, please enter 'yes' or 'no'.")
    else:
        print("Invalid input, please enter 'yes' or 'no'.")
