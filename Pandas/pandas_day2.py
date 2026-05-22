import pandas as pd

titanic = pd.read_csv("titanic/train.csv")

survival_by_gender = titanic.groupby('Sex')['Survived'].mean()*100
print(survival_by_gender)

survival_by_class = titanic.groupby('Pclass')['Survived'].mean()*100
print(survival_by_class)

# Q1: Select only the Name and Age columns
name_age = titanic.loc[:, ['Name', 'Age']]
print(name_age)
# Q2: Show all passengers older than 50
older_than_50 = titanic[titanic['Age'] > 50]
print(older_than_50)
# Q3: Show all female passengers who survived
female_survivors = titanic[(titanic['Sex'] == 'female') & (titanic['Survived'] == 1)]
print(female_survivors)
# Q4: What is the average fare paid by each class?
average_fare_by_class = titanic.groupby('Pclass')['Fare'].mean()
print(average_fare_by_class)
# Q5: How many passengers were in each class?
passengers_by_class = titanic['Pclass'].value_counts()
print(passengers_by_class)
# Q6: Select the first 10 rows using iloc
first_10_rows = titanic.iloc[:10]
print(first_10_rows)
# Q7: What is the oldest passenger's age?
oldest_age = titanic['Age'].max()
print(oldest_age)
# Q8: How many passengers had more than 2 siblings/spouses (SibSp)?
passengers_with_many_siblings = titanic[titanic['SibSp'] > 2]
print(passengers_with_many_siblings.shape[0])
# Q9: What was the average age of survivors vs non-survivors?
average_age_by_survival = titanic.groupby('Survived')['Age'].mean()
print(average_age_by_survival)
# Q10: Show passengers whose name contains "Miss"
miss_passengers = titanic[titanic['Name'].str.contains('Miss')]
print(miss_passengers)

# BUSINESS INSIGHT:
# The Titanic data reveals a clear class-based survival gap.
# First class survival: 63% — Second class: 47% — Third class: 24%
# Despite third class having the most passengers (491),
# they had the lowest survival rate.
# Wealthier passengers had better deck access and were
# prioritised during evacuation.