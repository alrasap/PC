#-----------------------------------------------------------------------------
# Name:        Frozen Sets and Immutability (frozensets.py)
# Purpose:     To demonstrate how frozensets work and show their immutability.
#
# Author:      Rohan
# Created:     04-Apr-2025
# Updated:     04-Apr-2025
#-----------------------------------------------------------------------------

# Step 1: Create a frozenset
frozen_numbers = frozenset({1, 2, 3, 4, 5})
print("Step 1: Frozenset created:", frozen_numbers)

# Step 2: Try to add an element to the frozenset
print("\nStep 2: Trying to add 6 to the frozenset...")
try:
    frozen_numbers.add(6)  # This will cause an error because frozensets are immutable
except AttributeError as e:
    print("Error:", e)  # Catch and display the error

# Step 3: Show that the frozenset remains unchanged
print("\nStep 3: Frozenset still contains:", frozen_numbers)

# Step 4: Ask if the user wants to try again or exit
while True:
    continue_choice = input("\nWould you like to explore again? (yes/no): ").strip().lower()
    if continue_choice == "yes":
        print("\nThe frozenset is immutable, so you cannot modify it!")
    elif continue_choice == "no":
        print("\nThanks for trying out frozensets! Goodbye!")
        break
    else:
        print("Please type 'yes' or 'no'.")
