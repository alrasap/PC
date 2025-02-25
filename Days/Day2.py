"""
Program Description:
This program asks the user for their name, age, and some other personal preferences. 
It uses the input() function to collect responses and the print() function to display the user's answers.
The program also prints some random questions and captures user responses for those as well.

Made by: Rohan Singh  
Student Number: 931006  
Date: February 14, 2025

"""

# Asking for user's basic information (name and age)
Name = input("What's your name?: ")  # Prompting the user to enter their name
AGE = input("How old are you?: ")    # Prompting the user to enter their age

# Printing the user's name and age
print()  # Creating an empty line for readability
print("Name:")  # Labeling the following print as 'Name'
print(Name)  # Displaying the name entered by the user
print("AGE")  # Labeling the following print as 'AGE'
print(AGE)  # Displaying the age entered by the user

# Adding more random questions and printing the responses
print()  # Adding a space for readability
print("More Random Questions")  # Printing a heading for the new section
print()  # Creating an empty line

# Asking the user for their comfort food, travel preference, and sunrise/sunset preference
comfort_food = input("What’s your go-to comfort food?:")  # Prompt for comfort food
Travel = input("If you could time travel, would you visit the past or the future?:")  # Prompt for time travel preference
sunset = input("Do you prefer sunrise or sunset?")  # Prompt for sunrise/sunset preference

# Printing the responses to the random questions
print()  # Creating a blank line for readability
print("comfort food")  # Labeling the next response as 'comfort food'
print(comfort_food)  # Displaying the user's response to the comfort food question
print("Travel:")  # Labeling the next response as 'Travel'
print(Travel)  # Displaying the user's response to the time travel question
print("sunset")  # Labeling the next response as 'sunset'
print(sunset)  # Displaying the user's response to the sunrise/sunset question

# Repeating the sunset question at the end (a little redundant)
print("Do you prefer sunrise or sunset?")  # Just printing the question again

