# -----------------------------------------------------------------------------
# Name:        Sorting and Reversing a List (Sorting_And_Reversing_A_List.py)
# Purpose:     To demonstrate sorting and reversing a list of fruits.
#              The list is first sorted in ascending order, then reversed
#              to show how the sorting works in both directions.
#
# Author:      Rohan
# Created:     24-Mar-2025
# Updated:     24-Mar-2025
# -----------------------------------------------------------------------------

# This is a list of fruits that we will work with
fruits = ['banana', 'apple', 'grape', 'kiwi', 'orange']


# Function to print the current list
def print_fruits(fruit_list):
    print("\nCurrent List of Fruits:")
    for fruit in fruit_list:
        print(fruit)
    print("\nThis is the list you will be working with. You can sort it, reverse it, or add new fruits.")


# Sorting the list in alphabetical order (ascending)
def sort_fruits():
    print("\nSorting the fruits in alphabetical order...")
    fruits.sort()  # Sorts in ascending order (alphabetically)
    print("The list has been sorted in ascending order.")
    print("Sorted Fruits:", fruits)


# Reversing the sorted list to get it in descending order
def reverse_fruits():
    print("\nReversing the sorted list to show it in descending order...")
    fruits.reverse()  # Reverses the list order
    print("The list has been reversed to descending order.")
    print("Reversed Sorted Fruits:", fruits)


# Ask the user if they would like to add more fruits
def add_fruit():
    print("\nYou can add a new fruit to the list!")
    new_fruit = input("Enter the name of the fruit you'd like to add (e.g., 'mango'): ").lower()
    fruits.append(new_fruit)  # Add the new fruit to the list
    print(f"\n{new_fruit.capitalize()} has been added to the list.")
    print("Updated List of Fruits:", fruits)


# Main function to control the flow
def main():
    print("Welcome to the Sorting and Reversing Fruit List Program!\n")
    print("You will be able to interact with a list of fruits and choose what you want to do with it.")

    while True:
        print_fruits(fruits)  # Display current fruits in the list

        # Provide a menu of options for the user
        user_choice = input("\nWhat would you like to do?\n"
                            "1. Sort the list alphabetically\n"
                            "2. Reverse the list to descending order\n"
                            "3. Add a new fruit to the list\n"
                            "4. Exit the program\n"
                            "Enter choice (1/2/3/4): ")

        if user_choice == '1':
            sort_fruits()  # Call the function to sort the fruits
        elif user_choice == '2':
            reverse_fruits()  # Call the function to reverse the fruits
        elif user_choice == '3':
            add_fruit()  # Call the function to add a new fruit
        elif user_choice == '4':
            print("\nThank you for using the program! Goodbye!\n")
            break  # Exit the program
        else:
            print("\nInvalid choice! Please enter 1, 2, 3, or 4.")


# Start the program
main()