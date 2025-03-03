# Program Name: Temperature Advice
# Purpose: This program takes the current temperature from the user and gives advice on what to wear based on the temperature.
# Creator: Rohan Singh
# Student Number: 931006
# Date: February 25, 2025

# This program helps the user decide what to wear based on the temperature in Celsius.
# The program uses conditional statements to check the temperature and provide appropriate clothing suggestions.

# Step 1: Ask the user to enter the current temperature in Celsius.
temperature = float(input("Enter the temperature: "))  # We use float to allow decimal values for temperature.

# Step 2: Use conditional statements to provide advice based on the temperature.


if temperature < 10:
    print(
        "It's cold outside. Wear a jacket!")  # If the temperature is below 10°C, the program suggests wearing a jacket.


elif 10 <= temperature <= 25:
    print(
        "It's a nice day. Wear short-sleeves!")  # If the temperature is between 10°C and 25°C, the program suggests wearing short-sleeves.


else:
    print("It's hot outside. Stay cool!")  # If the temperature is above 25°C, the program suggests staying cool.



