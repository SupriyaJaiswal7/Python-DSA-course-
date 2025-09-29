"""
Task 1: Python Printing Basics

Objective:
- Practice print statements, separators, end-of-line options
- Work with variables, formatting, and escape characters

Instructions:
1. Print simple text
2. Print multiple items with separators
3. Use end= parameter
4. Combine variables with f-strings and format()
5. Use escape characters (\n, \t, \")
6. Repeat strings with *
"""

# Step 1: Basic printing
print("Hello, Python World!")

# Step 2: Printing multiple items
print("Python", "DSA", "Course", sep=" | ")

# Step 3: Control end of print
print("Hello", end="... ")
print("World!")

# Step 4: Using variables
language = "Python"
version = 3.12
print(f"This is {language} version {version}")
print("This is {} version {}".format(language, version))

# Step 5: Escape characters
print("Line1\nLine2")
print("Tabbed\tText")
print("Quote: \"Python is fun\"")

# Step 6: Repetition
print("Repeat! " * 3)

# Step 7: Numbers + strings
num = 7
print("Number + 3 =", num + 3)
