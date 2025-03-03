'''
# Voting Eligibility Checker
# Purpose: This Python program asks the user for their age and checks if they are eligible to vote.
# Made by: Rohan Singh
# Student Number: 931006
# Date: February 27, 2025

# The program will:
# 1. Ask the user to input their age.
# 2. Store the input as a number in a variable.
# 3. Use a conditional statement to check if the person is 18 or older.
# 4. Print whether the person is eligible to vote or not.
'''
# Step 1: Ask the user to enter their age
# The input() function takes user input. We convert it into an integer using int().
user_input = input("Enter your age: ")  # Prompting the user to enter their age
# Step 2: Store the age in a variable
# We store the user input as an integer in the variable 'age'.
age = int(user_input)  # Convert the input into an integer and store it
# Step 3: Use a conditional statement to check if the person can vote
# A person is eligible to vote if their age is 18 or more.
if age >= 18:  # If the age is 18 or more, they can vote
    # Step 4: If the person is eligible, print "You are eligible to vote!"
    print("You are eligible to vote!")  # Output message for eligible voters
else:  # If the person is younger than 18
    # Step 5: If the person is not eligible, print "Sorry, you are not eligible to vote yet."
    print("Sorry, you are not eligible to vote yet.")  # Output message for ineligible voters

