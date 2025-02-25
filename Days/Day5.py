# Code created by Rohan Singh, student number 931006
# Date: February 19, 2025
# This script asks for a user's input and provides a response based on what they enter.
# The first part is based on a tutorial where it checks if the user's name is "Rohan".
# The second part is what the user tries to do, where it checks if the username entered is "111".

# What the tutorial shows:
# Asking the user for their name and providing a response based on whether their name is "Rohan".

myName = input("What's your name?: ")  # Prompt the user for their name and store the input in the variable 'myName'
if myName == "Rohan":  # Check if the user's name is "Rohan"
    print("Welcome dude!")  # If the name is "Rohan", print a welcoming message
    print("You're just the coolest man")  # Print a second message for "Rohan"
else:
    print("Who are you")  # If the name is not "Rohan", print a different message

# What you tried to do:
# Asking the user for a "username" and providing a response based on whether the username is "111".

username = input("Username: ")  # Prompt the user for a username and store the input in the variable 'username'
if username == "111":  # Check if the username entered is "111"
    print("That good")  # If the username is "111", print a message saying "That good"
else:
    print("Bye bye")  # If the username is not "111", print "Bye bye"
