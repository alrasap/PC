# -----------------------------------------------------------------------------
# Name:        Tuple Basics (Tuple_Basics.py)
# Purpose:     To demonstrate the basic usage of tuples in Python,
#              including creating, accessing, and extracting elements from tuples.
#
# Author:      Rohan
# Created:     26-Mar-2025
# Updated:     27-Mar-2025
# -----------------------------------------------------------------------------

# Step 1: Create a tuple with five different elements.
# The elements will include an integer, a float, a string, a boolean, and another tuple.
my_tuple = (42, 3.14, 'Python', True, (1, 2, 3))


# List of exploration options for the tuple
def explore_tuple_experience(explore_count):
    """
    Function to demonstrate different operations on the tuple depending on how many times the user has explored.
    """
    if explore_count == 1:
        print("\nThe entire tuple:", my_tuple)
        third_element = my_tuple[2]
        print("The third element is:", third_element)
        nested_tuple = my_tuple[4]
        first_element_of_nested_tuple = nested_tuple[0]
        print("The first element of the nested tuple is:", first_element_of_nested_tuple)

    elif explore_count == 2:
        tuple_length = len(my_tuple)
        print("\nThe length of the tuple is:", tuple_length)
        print("The second element of the tuple is:", my_tuple[1])

    elif explore_count == 3:
        check_value = 'Python'
        if check_value in my_tuple:
            print(f"\nThe value '{check_value}' is present in the tuple at index {my_tuple.index(check_value)}.")
        else:
            print(f"\nThe value '{check_value}' is not present in the tuple.")

    elif explore_count == 4:
        print("\nThe entire tuple:", my_tuple)
        reversed_tuple = my_tuple[::-1]
        print("Reversed tuple:", reversed_tuple)

    else:
        print("\nYou've explored the tuple enough for now. Thank you!")


# Function to handle user interaction
def user_interaction():
    """
    This function manages the user's input to decide if they want to continue exploring tuples.
    It repeats until the user chooses to stop.
    """
    explore_count = 1  # Keep track of how many times the user has explored

    while True:
        # Ask the user if they want to continue exploring tuples.
        continue_choice = input("\nWould you like to continue exploring tuples? (yes/no): ").lower()

        if continue_choice == "yes":
            print("\nAwesome! Let's explore more about tuples!\n")
            explore_tuple_experience(explore_count)  # Call the function to explore the tuple with variation
            explore_count += 1  # Increment the explore count for the next round
        elif continue_choice == "no":
            print("\nThanks for exploring tuples! Goodbye.\n")
            break  # Exit the loop and end the program
        else:
            print("\nInvalid input. Please type 'yes' or 'no'.")


# Initial call to the explore_tuple_experience function
explore_tuple_experience(1)

# Start the user interaction loop
user_interaction()
