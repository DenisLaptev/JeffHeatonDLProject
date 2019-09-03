import os
import pandas as pd

# Missing Values

'''
Missing values are a reality of machine learning.
Ideally every row of data will have values for all columns.
However, this is rarely the case. Most of the values are present in the MPG database.
However, there are missing values in the horsepower column.
A common practice is to replace missing values with the median value for that column.
'''

URL = "https://data.heatonresearch.com/data/t81-558/auto-mpg.csv"

# The following code replaces any NA values in horsepower with the median

df = pd.read_csv(URL, na_values=['NA', '?'])

print(f"horsepower has na? {pd.isnull(df['horsepower']).values.any()}")

#print(df)

print("Filling missing values...")

med = df['horsepower'].median()

df['horsepower'] = df['horsepower'].fillna(med)

# df = df.dropna() # you can also simply drop NA values

print(f"horsepower has na? {pd.isnull(df['horsepower']).values.any()}")

#print(df)
