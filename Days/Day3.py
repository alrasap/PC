# Code created by Rohan Singh, student number 931006
# Date: February 17, 2025
# This script collects information from the user about their name, lunch, drink, and mood,
# then prints out a customized message based on their input.
# The first part of the code mimics a tutorial example, and the second part is an extended version
# where the user is asked more questions, and the input is used to create a personalized message.

# Section 1: Basic example from the tutorial
# Asking the user for their name and lunch, and then displaying a personalized message

myName = input("What's your name: ")  # Prompt user for their name and store the response in variable 'myName'
myLunch = input("What are you having for lunch?: ")  # Prompt user for their lunch and store it in 'myLunch'
print()  # Blank line for separation in the output
print()  # Another blank line for a cleaner output
# Print a message combining the user's name and lunch choice
print(myName, "is going to be chowing down on", myLunch, "very soon!")

# Section 2: Extended example (my version of the code)
# Asking the user for their name, drink, and mood, then displaying a personalized message with all the details

yourName = input("What's your name?: ")  # Prompt user for their name and store it in 'yourName'
yourDrink = input("What drink are you having with your meal?: ")  # Ask the user what drink they are having with their meal
yourMood = input("How are you feeling today?: ")  # Ask the user how they are feeling today
print()  # Blank line for separation in the output
print()  # Another blank line for a cleaner output
# Print a message using all the user inputs (name, mood, and drink) to create a personalized output
print(yourName, "is in a", yourMood, "mood and will be enjoying a delicious meal with some", yourDrink, "soon!")

# Explanation of changes:
# In the second section, I added three new inputs: 'yourName', 'yourDrink', and 'yourMood'.
# The final message now combines all three to make it more personal and detailed:
# "yourName is in a yourMood mood and will be enjoying a delicious meal with some yourDrink soon!"
