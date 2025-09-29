"""
Task 2: Type Checking and Type Conversion

Objective:
- Understand how to check the type of a variable using type()
- Learn how to check memory location with id()
- Convert values between int, float, and str using built-in functions

Instructions:
1. Take a number as input
2. Print its type and id
3. Convert it into another type (int → float, float → str, etc.)
4. Print the new value, type, and id
"""

# Step 1: Take input from user (always string by default)
num = input("Enter a number: ")

# Step 2: Convert input to integer
num_int = int(num)
print("Integer Value:", num_int)
print("Type:", type(num_int))
print("ID:", id(num_int))

# Step 3: Convert integer to float
num_float = float(num_int)
print("Float Value:", num_float)
print("Type:", type(num_float))
print("ID:", id(num_float))

# Step 4: Convert float to string
num_str = str(num_float)
print("String Value:", num_str)
print("Type:", type(num_str))
print("ID:", id(num_str))
