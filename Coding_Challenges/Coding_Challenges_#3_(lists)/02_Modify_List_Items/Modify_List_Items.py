# -----------------------------------------------------------------------------
# Name:        Grocery List Modifier (grocery_list.py)
# Purpose:     This Python program modifies a grocery list by changing an existing item
#              (specifically, changing 'bananas' to 'grapes') and prints the updated list.
#              It also accesses and prints the third item in the list, and prompts the user
#              if they want to continue modifying the list. It prevents adding an item if it's
#              already in the list.
#
# Author:      Rohan
# Created:     20-Mar-2025
# Updated:     20-Mar-2025
# -----------------------------------------------------------------------------
# Program Flow:
# 1. Define a list of grocery items.
# 2. Modify the list by changing 'bananas' to 'grapes'.
# 3. Print the updated list.
# 4. Access and print the third item (index 2) in the list.
# 5. Ask the user if they want to modify the list again.
# 6. If they want to add a new item, check if it already exists before adding.
# 7. Exit the program if the user doesn't want to modify the list anymore.

# Step 1: Initial grocery list
grocery_list = ['apples', 'bananas', 'carrots', 'milk', 'bread']

# Step 2: Modify the list by changing 'bananas' to 'grapes'
grocery_list[1] = 'grapes'

# Step 3: Print the updated grocery list
print("Updated Grocery List:")
print(grocery_list)  # Display the modified list

# Step 4: Access and print the third item (index 2) in the list
third_item = grocery_list[2]
print("\nThe third item in the list is:", third_item)  # Show the third item

# Step 5: Ask the user if they'd like to modify the list again
while True:
    user_input = input("\nWould you like to modify the list again? (yes/no): ").strip().lower()

    if user_input == 'yes':
        # Allow the user to specify what item they want to change
        item_to_change = input("\nWhich item would you like to modify? ").strip().lower()

        if item_to_change in grocery_list:
            new_item = input(f"\nWhat would you like to change '{item_to_change}' to? ").strip()
            index = grocery_list.index(item_to_change)
            grocery_list[index] = new_item
            print("\nUpdated Grocery List:", grocery_list)
        else:
            print(f"\n'{item_to_change}' not found in the list. Please check the spelling.")

        # Ask if the user wants to add a new item
        add_item = input("\nWould you like to add a new item to the list? (yes/no): ").strip().lower()
        if add_item == 'yes':
            new_item = input("\nWhat item would you like to add? ").strip().lower()

            # Prevent adding an item that's already in the list
            if new_item in grocery_list:
                print(f"\n'{new_item}' is already in the list. Please choose a different item.")
            else:
                grocery_list.append(new_item)
                print(f"\n'{new_item}' has been added to the list!")
                print("Updated Grocery List:", grocery_list)

    elif user_input == 'no':
        # If the user doesn't want to modify the list anymore, exit the loop
        print("\nThank you for using the program. Have a great day!")
        break
    else:
        # Handle invalid input
        print("\nPlease enter 'yes' or 'no'.")
