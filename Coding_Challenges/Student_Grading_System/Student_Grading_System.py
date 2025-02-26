'''
Program Name: student_grading.py
Purpose: This program takes a student's score and determines their grade.
Creator: Rohan, Singh
Date: Monday, february,24, 2025
'''

import sys

def get_score():
    """Retrieve score from input or command-line argument."""
    if len(sys.argv) > 1:
        try:
            return int(sys.argv[1])
        except ValueError:
            print("Invalid input. Please provide a number.")
            sys.exit(1)
    else:
        try:
            return int(input("Enter your score (out of 100): "))
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 100.")
            return get_score()

# Get user input or command-line argument
score = get_score()

# Determine the grade based on the score using conditionals
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


