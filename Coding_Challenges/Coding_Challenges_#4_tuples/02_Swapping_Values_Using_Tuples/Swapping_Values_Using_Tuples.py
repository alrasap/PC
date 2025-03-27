# -----------------------------------------------------------------------------
# Name:        Swapping Values Using Tuples (swap_values.py)
# Purpose:     To demonstrate how to swap values using tuples in Python
#              without using a temporary variable.
#              This program takes two numbers from the user,
#              swaps them using tuples, and prints the swapped values.
#
# Author:      Rohan
# Created:     27-Mar-2025
# Updated:     27-Mar-2025
# -----------------------------------------------------------------------------

# Function to swap values using tuples
def swap_values():
    """
    This function asks the user to input two numbers,
    stores them in a tuple, swaps them and displays the result.
    """
    # Get user input for the first number
    while True:
        try:
            num1 = int(input("Enter first number: "))
            break  # Exit loop if input is valid
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Get user input for the second number
    while True:
        try:
            num2 = int(input("Enter second number: "))
            break  # Exit loop if input is valid
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Swap the numbers using a tuple
    swapped_values = (num2, num1)  # The tuple holds the swapped values

    # Print the swapped values in a user-friendly format
    print(f"\nSwapped values: {swapped_values[0]} and {swapped_values[1]}")


# Ask the user if they want to continue after each swap
def main():
    """
    Main function to handle the flow of the program.
    Greets the user, asks for numbers, performs the swap,
    and then asks if the user wants to continue.
    """
    # Greet the user with a welcome message
    print("Welcome to the Value Swapping Program!")
    print("This program swaps the values of two numbers using tuples.\n")

    # Loop for continuing the program until the user decides to stop
    while True:
        # Call the swap function
        swap_values()

        # Ask if the user wants to swap another pair of values
        continue_choice = input("\nWould you like to swap another pair of values? (yes/no): ").lower()

        # Handle user input and exit or continue
        if continue_choice == 'no':
            print("\nThank you for using the program! Goodbye!")
            break
        elif continue_choice != 'yes':
            print("\nInvalid input! Please type 'yes' or 'no'.\n")


# Run the main function to start the program
if __name__ == "__main__":
    main()
