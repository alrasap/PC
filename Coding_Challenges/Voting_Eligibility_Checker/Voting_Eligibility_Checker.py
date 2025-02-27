user_input = input("enter your age: ")

number = int(user_input)

if number % 18 == 0:
    print("You are eligible to vote!")
else:
    print("Sorry, you are not eligible to vote yet.")
