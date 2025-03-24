## Grocery List Program

### Purpose:
This Python program allows the user to create and manage a grocery list. It starts with some predefined items and lets the user add more items interactively. The program ensures that no duplicates are added and provides a friendly user interface to interact with.

### Created by:
Rohan   
Student Number: 931006  
Date: March 20, 2025

### Requirements:
* Python 3.x

### Instructions:
1. Run the program.
2. The program will display an initial list of grocery items.
3. It will ask if you'd like to add more items.
4. If you say **yes**, you'll be prompted to enter the name of the item you'd like to add.
5. If the item is already in the list, the program will inform you and will not add it again.
6. The program will continue asking if you'd like to add more items until you say **no**.
7. When you say **no**, it will ask if you're done adding items. If you say **yes**, the program will thank you and end. If you say **no**, the program will allow you to keep adding more items.

### Example Output:

```python
This is what you have right now in your grocery list:
['apples', 'bread', 'milk', 'eggs', 'cheese', 'tomatoes']
Do you want to add more items to the list? (yes/no): yes
What item would you like to add? milk
milk is already in the list. Please add a different item.
Updated Grocery List: ['apples', 'bread', 'milk', 'eggs', 'cheese', 'tomatoes']
Do you want to add more items to the list? (yes/no): yes
What item would you like to add? oranges
oranges has been added to the list.
Updated Grocery List: ['apples', 'bread', 'milk', 'eggs', 'cheese', 'tomatoes', 'oranges']
Do you want to add more items to the list? (yes/no): no
Is that all for now? (yes/no): no
You can continue adding items at any time. Let's add more!
Do you want to add more items to the list? (yes/no): no
Is that all for now? (yes/no): yes
Thank you for using the grocery list program!
