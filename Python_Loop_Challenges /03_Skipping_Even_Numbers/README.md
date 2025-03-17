## Skipping Even Numbers

### Purpose:
This Python program prints the numbers from 1 to 10 but skips the even numbers. 
It uses a `for` loop and the `continue` statement to achieve this.

### Created by:
Rohan Singh  
Student Number: 931006  
Date: March 17, 2025

### Requirements:
* Python 3.x

### Instructions:
1. Run the program.
2. The program will print numbers from 1 to 10.
3. It will skip even numbers and only print the odd numbers (1, 3, 5, 7, 9).


### Explanation:
- The program uses a `for` loop to iterate through numbers from 1 to 10.
- It checks if the number is even (i.e., divisible by 2). If it is, the program uses the `continue` statement to skip to the next iteration without printing the even number.
- Only odd numbers (1, 3, 5, 7, 9) are printed.

### Code Walkthrough:
1. The `for` loop starts with `range(1, 11)`, which means it will loop through numbers from 1 to 10.
2. Inside the loop, we check if the number is even using `if number % 2 == 0`.
3. If the condition is true, the `continue` statement is executed, which skips the current iteration.
4. If the number is odd, the `print(number)` line will execute, printing the number to the screen.
