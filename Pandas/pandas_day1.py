import pandas as pd

marks = pd.Series([85, 92, 78, 65, 90], index=["Supriya", "Rahul", "Priya", "Vikram", "Sneha"])
print(marks)
print(f"Highest mark: {marks.max()}")
print(f"Lowest mark: {marks.min()}")
print(f"Average mark: {marks.mean():.2f}")

data = {
    "Name": ["Supriya", "Rahul", "Priya", "Vikram", "Sneha"],
    "Marks": [85, 92, 78, 65, 90],
    "Passed":[True, True, True, False, True]
}

df = pd.DataFrame(data)
print(df)
print(f"\nShape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")

# Reading a real CSV file
titanic = pd.read_csv(r"D:\Documents\Projects\python_learning_journey\Pandas\titanic\train.csv")

# Five things you always check with new data
print(titanic.shape)
print(titanic.head())
print(titanic.dtypes)
print(titanic.isnull().sum())
print(titanic.describe())