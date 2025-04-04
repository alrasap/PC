#-----------------------------------------------------------------------------
# Name:        Adding and Removing Elements (3_Adding_Removing_Elements.py)
# Purpose:     To demonstrate how to add and remove elements from a set using
#              the .add(), .remove(), and .discard() methods.
#
# Author:      Rohan
# Created:     April 3, 2025
# Updated:     April 3, 2025
#-----------------------------------------------------------------------------
# This program starts with a set of numbers, adds and removes elements,
# then prints the updated set.

# Step 1: Create an initial set of numbers
numbers = {1, 2, 3, 4, 5}  # Starting set

# Step 2: Add elements to the set using the .add() method
numbers.add(6)  # Adds 6 to the set
numbers.add(7)  # Adds 7 to the set

# Step 3: Remove an element using the .remove() method
numbers.remove(2)  # Removes 2 from the set. If 2 is not in the set, it will cause an error.

# Step 4: Print the updated set
print("Updated set after adding and removing elements:", numbers)

# Optional: If you want to remove an element without causing an error if it's not present, use .discard()
# numbers.discard(3)  # Removes 3 from the set, doesn't raise an error if 3 is not present
