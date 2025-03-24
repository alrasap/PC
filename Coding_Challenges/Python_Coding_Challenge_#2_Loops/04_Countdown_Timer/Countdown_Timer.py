# Program Name: Countdown Timer
# Purpose: This program counts down from 10 to 1. If the user types "stop", the countdown stops.
# Creator: Rohan
# Student Number: 931006
# Date: March 10, 2025

# Start of the countdown at 10
count = 10

# The while loop will continue until the count reaches 1 or the user types "stop"
while count > 0:
    # Print the current count
    print(count)

    # Ask the user to type "stop" to cancel or press Enter to continue
    user_input = input('Enter "stop" to cancel or press Enter: ')

    # If the user enters "stop", the loop will break
    if user_input.lower() == 'stop':
        print("Countdown stopped!")
        break  # Exit the loop

    # Decrease the count by 1 for the next loop
    count -= 1

# Once the loop ends, the program has finished.
