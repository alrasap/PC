# -----------------------------------------------------------------------------
# Name:        Tuple Operations & Count (tuple_operations.py)
# Purpose:     To count how many times a specific fruit appears in a tuple
#              based on user input, while handling invalid input gracefully.
#
# Author:      Rohan
# Created:     27-Mar-2025
# Updated:     27-Mar-2025
# -----------------------------------------------------------------------------

# List of fruits in the tuple
fruit_tuple = ("apple", "banana", "apple", "cherry", "banana", "apple")


# Function to count the occurrences of a fruit
def count_fruit(fruit):
    # Using the count() method to find how many times the fruit appears in the tuple
    return fruit_tuple.count(fruit)


# Function to check if the input is valid
def is_valid_fruit(fruit):
    # A valid fruit is a string that's in the list of fruits in the tuple
    return fruit in fruit_tuple


# Function to interact with the user
def main():
    print("Welcome to the Fruit Counter program!")

    # Asking the user to input the fruit name with a simple prompt
    fruit = input("Enter a fruit name (e.g., 'apple', 'banana', 'cherry'): ").lower()

    # Keep prompting until the user enters a valid fruit from the tuple
    while not is_valid_fruit(fruit):
        print(f"Sorry, '{fruit}' is not in the tuple.")
        fruit = input("Please enter a valid fruit name (e.g., 'apple', 'banana', 'cherry'): ").lower()

    # Once a valid fruit is entered, check how many times it appears in the tuple
    count = count_fruit(fruit)

    # Printing the result
    print(f"'{fruit}' appears {count} times in the tuple.")

    # Ask the user if they want to continue
    continue_prompt = input("Would you like to check another fruit? (yes/no): ").lower()

    if continue_prompt == "yes":
        main()  # Restart the program if user chooses 'yes'
    else:
        print("Thank you for using the Fruit Counter program! Goodbye!")


# Call the main function to run the program
if __name__ == "__main__":
    main()
