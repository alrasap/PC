# Day of the Week Activity Recommender
# Purpose: This program asks the user for the current day of the week and suggests an activity based on the day.
# Made by: Rohan , Student Number 931006
# Date: march 3, 2025
# This code was based on a tutorial and further worked on by me. I used basic concepts like conditionals (if-else statements).

# Ask the user to input the day of the week
# We use input() to get what the user types and store it in a variable called 'day'
day = input("Enter the day of the week: ")

# Check the value of 'day' and suggest an activity based on the day
# If the user enters "Monday", suggest working out
if day == "Monday":
    print("Start your week with a workout!")  # Suggest activity for Monday
# If the user enters "Tuesday", suggest reading a book
elif day == "Tuesday":
    print("It's a great day to read a book!")  # Suggest activity for Tuesday
# If the user enters "Wednesday", suggest watching a movie
elif day == "Wednesday":
    print("Mid-week movie night!")  # Suggest activity for Wednesday
# If the user enters "Thursday", suggest trying a new recipe
elif day == "Thursday":
    print("Try a new recipe!")  # Suggest activity for Thursday
# If the user enters "Friday", suggest relaxing for the weekend
elif day == "Friday":
    print("Relax and enjoy the weekend!")  # Suggest activity for Friday
# If the user enters "Saturday", suggest going for a hike
elif day == "Saturday":
    print("Go for a hike!")  # Suggest activity for Saturday
# If the user enters "Sunday", suggest preparing for the week ahead
elif day == "Sunday":
    print("Prepare for the week ahead with some self-care.")  # Suggest activity for Sunday
# If the user doesn't enter a valid day, let them know it's an invalid input
else:
    print("Please enter a valid day of the week.")  # Handle invalid input

