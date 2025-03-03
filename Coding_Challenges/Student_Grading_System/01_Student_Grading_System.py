'''
Program Name: student grading
Purpose: This program asks the user for a score and gives a grade.
Creator: Rohan, Singh (Student Number: 931006)
Date: February 24, 2025
'''
# Ask the user to type a score (a number from 0 to 100)
score = int(input("Type your score (0 to 100): "))
# Check the score and give the correct grade
if score >= 90:  # If score is 90 or more, give an A
    print("Your grade is A.")
if score >= 80 and score < 90:  # If score is 80 to 89, give a B
    print("Your grade is B.")
if score >= 70 and score < 80:  # If score is 70 to 79, give a C
    print("Your grade is C.")
if score >= 60 and score < 70:  # If score is 60 to 69, give a D
    print("Your grade is D.")
if score < 60:  # If score is less than 60, give an F
    print("Your grade is F.")
