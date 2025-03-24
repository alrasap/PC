#-----------------------------------------------------------------------------
# Name:        Remove Items from a List (remove_items_from_list.py)
# Purpose:     To demonstrate how to remove items from a list in Python.
#              This program removes specific items from a to-do list and
#              prints the list at each stage.
#
# Author:      Rohan
# Created:     March 20, 2025
# Updated:     March 20, 2025
#-----------------------------------------------------------------------------

# This program demonstrates how to remove items from a list in Python.
# We will create a to-do list, remove specific items from the list, and then print the updated list.
# The user will also be asked if they want to continue after the program finishes removing the items.

# Step 1: Create a list with some to-do items
todo_list = ['write email', 'finish homework', 'call mom', 'clean room']

# Step 2: Print the original list to show the initial state
print("Original list:", todo_list)

# Step 3: Remove 'call mom' from the list
# The remove() method removes the first occurrence of the item in the list.
todo_list.remove('call mom')  # This removes 'call mom' from the list
print("\nList after removing 'call mom':", todo_list)

# Step 4: Remove 'clean room' from the list
# Again, we use remove() to delete 'clean room' from the list.
todo_list.remove('clean room')  # This removes 'clean room' from the list
print("\nFinal list after removing 'clean room':", todo_list)

# Step 5: Ask the user if they want to continue or end the program
continue_choice = input("\nWould you like to continue (yes/no)? ")

# Step 6: Respond based on user's input
if continue_choice.lower() == 'yes':
    print("\nThank you for using the list remover program!")
    print("You can now continue modifying or checking your list.")
else:
    print("\nGoodbye! Have a great day and stay productive!")
