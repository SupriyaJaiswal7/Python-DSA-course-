import pandas as pd

def clean_titanic(filepath):
    """
    Loads and cleans the Titanic dataset.
    Steps:
    1. Fill Embarked with most common port
    2. Fill Age with median age
    3. Drop Cabin column (77% missing)
    """
    df = pd.read_csv(filepath)
    
    print(f"Before cleaning: {df.shape}")
    print(f"Missing values:\n{df.isnull().sum()}\n")
    
    # Fix 1: Embarked — fill with mode
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    
    # Fix 2: Age — fill with median
    df['Age'] = df['Age'].fillna(df['Age'].median())
    
    # Fix 3: Cabin — drop entirely (77% missing)
    df = df.drop('Cabin', axis=1)
    
    print(f"After cleaning: {df.shape}")
    print(f"Missing values:\n{df.isnull().sum()}")
    
    return df

# Run it
titanic_clean = clean_titanic("titanic\train.csv")

# DAY 3 OBSERVATIONS — DATA CLEANING
#
# Dataset before cleaning: 891 rows, 12 columns
# Dataset after cleaning: 891 rows, 11 columns
#
# THREE COLUMNS HAD MISSING DATA — THREE DIFFERENT SOLUTIONS:
#
# 1. EMBARKED — 0.2% missing (only 2 rows)
#    Solution: Fill with mode (most common value = 'S' for Southampton)
#    Why: When very few values are missing, filling with the most
#    common value is safe — it does not distort the data
#
# 2. AGE — 20% missing (177 rows)
#    Solution: Fill with median (28 years)
#    Why: Cannot drop 177 rows — too much data lost.
#    Used median not mean because a few very old or very young
#    passengers would pull the mean in the wrong direction.
#    Median is more resistant to outliers.
#
# 3. CABIN — 77% missing (687 rows)
#    Solution: Drop the entire column
#    Why: 77% missing means the column is mostly empty.
#    Filling it would mean inventing data we do not have.
#    The absence of cabin data itself told us something —
#    third class passengers had no cabins assigned.
#    But the column cannot be used for analysis.
#
# KEY LESSON:
# Missing data is not always random.
# Always ask WHY data is missing before deciding what to do.
# Different columns need different treatments.
# Never blindly fill or drop without understanding the reason.
#
# AFTER CLEANING:
# All 11 remaining columns have 0 missing values.
# The dataset is now ready for analysis and visualisation.