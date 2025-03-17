# Program Name: Skipping Even Numbers
# Purpose: This program prints numbers from 1 to 10 but skips even numbers using the continue statement.
# Creator: Rohan Singh
# Student Number: 931006
# Date: March 17, 2025

# Start a for loop from 1 to 10
for number in range(1, 11):
    # Check if the number is even
    if number % 2 == 0:
        continue  # Skip this number if it's even
    print(number)  # Print the number if it's odd
