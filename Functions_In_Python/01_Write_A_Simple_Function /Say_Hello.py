# -----------------------------------------------------------------------------
# Name:        Say Hello (Say_Hello.py)
# Purpose:     To demonstrate how to write and use a simple function in Python
#              that prints a greeting message to the user.
#
# Author:      Rohan
# Created:     Apr 29, 2025
# Updated:     Apr 29, 2025
# -----------------------------------------------------------------------------

# This function is called 'say_hello'. It doesn't take any inputs.
# When you call this function, it will print "Hello, world!" on the screen.
def say_hello():
    print("Hello, world!")


# Call the function to see the message
say_hello()

# Ask the user if they want to run the function again
while True:
    answer = input("Would you like to say hello again? (yes/no): ").strip().lower()

    if answer == "yes":
        say_hello()
    elif answer == "no":
        print("Alright, goodbye! 👋")
        break
    else:
        print("Please enter 'yes' or 'no'.")
