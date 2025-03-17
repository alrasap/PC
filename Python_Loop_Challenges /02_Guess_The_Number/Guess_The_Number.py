# Program Name: Guess the Number
# Purpose: This program generates a random number between 1 and 10 and keeps asking the user to guess it using a while loop until they guess correctly.
# Creator: Rohan Singh
# Student Number: 931006
# Date: March 17, 2025

import random  # Importing the random module to generate a random number

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)

# Variable to keep track of whether the user has guessed correctly
guess = None

# While loop to keep asking the user for their guess until it is correct
while guess != random_number:
    # Ask the user to input their guess
    guess = int(input("Guess the number between 1 and 10: "))  # Converting user input to an integer

    # Check if the guess is correct or not
    if guess != random_number:
        print("Wrong, try again!")  # If the guess is wrong, print this message
    else:
        print("Correct! 🎉")  # If the guess is correct, print this message
