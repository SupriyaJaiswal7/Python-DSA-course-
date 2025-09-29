"""
Task for Day 1

CLI Student Calculator (v0.1)

Problem Statement:
Write a Python program that acts like a mini calculator for students.
The program should take a student’s name as input.
Then, ask for two subject marks (integers, 0–100).
Print:
Their total
Their average
The difference between the two marks
Their percentage (out of 200) rounded to 2 decimal places


Sample Run:
Enter your name: Supriya
Enter marks for Subject 1: 85
Enter marks for Subject 2: 90
Hello Supriya 👋
Total = 175
Average = 87.5
Difference = 5
Percentage = 87.50 %


⚡️ Bonus (Optional, if you want harder):
Add a grade system (≥90 = A, ≥75 = B, ≥50 = C, else Fail).
Show everything in a formatted block.

"""

#Taking Student's Name as Input
name = input("Enter your name: ").strip()

#Taking 2 Subject Marks as Input
subject1 = int(input("Enter marks for Subject 1: "))
subject2 = int(input("Enter marks for Subject 2: "))
 
#Calculating Total,Average,Difference and Percentage of Student Marks
Total = subject1 + subject2
Average = Total / 2
Difference = abs(subject1 - subject2)
Percentage = (Total/200)*100
Percentage = round(Percentage, 2)

#Printing Output 
print(f"\n📘 Student Report for {name}\n")
print(f"Your total marks are: {Total}")
print(f"Average of your marks is: {Average}")
print(f"Percentage: {Percentage} %")

#For the bonus challenge going to add a grade system using if statement 

#First making it for subject 1
if subject1 >= 90:
    print("Your grade for subject 1 is: A")
elif subject1 >= 75:
    print("Your grade for subject 1 is: B")
elif subject1 >= 50:
    print("Your grade for subject 1 is: C")
else:
    print("You are fail in subject 1!")

#Now for subject 2
if subject2 >= 90:
    print("Your grade for subject 2 is: A")
elif subject2 >= 75:
    print("Your grade for subject 2 is: B")
elif subject2 >= 50:
    print("Your grade for subject 2 is: C")
else:
    print("You are fail in subject 2!")

#Now for the total Percentage
if  Percentage>= 90:
    print("Your overall grade is: A")
elif Percentage >= 75:
    print("Your overall grade is: B")
elif Percentage >= 50:
    print("Your overall grade is: C")
else:
    print("You should cry! 🙂")