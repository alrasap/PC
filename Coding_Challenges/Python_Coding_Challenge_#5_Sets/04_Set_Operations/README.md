# Set Operations in Python

### Purpose:
This Python program demonstrates how to perform basic **set operations** using Python. The set operations covered are:
- **Union**: Combining all elements from two sets.
- **Intersection**: Finding common elements between two sets.
- **Difference**: Identifying elements that are in one set but not in another.

The program provides an interactive experience where you can see the results of these operations and choose to perform them again.

### Created by:
**Rohan**  
Student Number: 931006  
Date: April 4, 2025

### Requirements:
- Python 3.x or higher

### Instructions:
1. **Run the Program**:
   - Execute the `set_operations.py` script in your Python environment.

2. **Set Operations**:
   - The program will automatically define two sets, `set1` and `set2`, as:
     ```python
     set1 = {1, 2, 3, 4}
     set2 = {3, 4, 5, 6}
     ```
   - It will then perform three operations:
     - **Union**: Combines all unique elements from both sets.
     - **Intersection**: Finds elements common to both sets.
     - **Difference**: Identifies elements present in `set1` but not in `set2`.

3. **View Results**:
   - After the operations are performed, the program will display the results:
     - **Union** of the sets
     - **Intersection** of the sets
     - **Difference** of the sets

4. **Interactive Mode**:
   - After displaying the results, the program will ask:
     - Would you like to perform another set operation?  
     Type **"yes"** to perform the operations again, or **"no"** to exit the program.

### Example Output:
```python
--- Results of Set Operations ---
Union: {1, 2, 3, 4, 5, 6}
Intersection: {3, 4}
Difference: {1, 2}

Would you like to perform another set operation? (yes/no): yes

Let's perform more set operations!

--- Results of Set Operations ---
Union: {1, 2, 3, 4, 5, 6}
Intersection: {3, 4}
Difference: {1, 2}

Would you like to perform another set operation? (yes/no): no

Thank you for using the Set Operations program. Goodbye!
