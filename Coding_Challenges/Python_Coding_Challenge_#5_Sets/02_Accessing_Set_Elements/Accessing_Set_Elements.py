#-----------------------------------------------------------------------------
# Name:        Set Elements Access (set_elements.py)
# Purpose:     To demonstrate how to access and iterate over elements in a set.
#              This program will create a set of colors and use a loop to print each color.
#
# Author:      Rohan
# Created:     02-Apr-2025
# Updated:     02-Apr-2025
#-----------------------------------------------------------------------------
# This program will create a set of colors and use a loop to print each color.
# Note that sets are unordered and unindexed, so the order may vary.

# Step 1: Create the set of colors
colors = {'red', 'blue', 'green', 'yellow'}

# Step 2: Use a loop to print each color
print("Here are the colors in the set:")

# The loop will iterate over each element in the set
for color in colors:
    print(color)

# Step 3: After displaying the colors, ask if the user wants to continue
continue_choice = input("\nWould you like to see the colors again? (yes/no): ")

# If the user answers 'yes', the program will repeat the process
while continue_choice.lower() == 'yes':
    print("\nHere are the colors again:")
    for color in colors:
        print(color)
    continue_choice = input("\nWould you like to see the colors again? (yes/no): ")

# If the user answers 'no', the program will exit
print("\nThank you for using the color set program! Goodbye!")
