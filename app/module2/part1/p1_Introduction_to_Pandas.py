import os
import pandas as pd

# The following code loads the MPG dataset into a dataframe.
# MPG dataset contains data for 398 cars,
# including mpg (miles per galon), cylinders, horsepower, ...

URL = "https://data.heatonresearch.com/data/t81-558/auto-mpg.csv"

# Simple dataframe
df = pd.read_csv(URL)
print(df[0:5])

print('------------------------------')
print()

# It is possible to generate a second dataframe
# to display statistical information about the first dataframe.

# Strip non-numerics
df = df.select_dtypes(include=['int', 'float'])

column_names = list(df.columns.values)
fields = []

for column_name in column_names:
    fields.append({
        'name': column_name,
        'mean': df[column_name].mean(),
        'var': df[column_name].var(),
        'sdev': df[column_name].std()
    })

for field in fields:
    print(field)

print('------------------------------')
print()

# Converting this to a dataframe allows for a nicer display.
df2 = pd.DataFrame(fields)
print(df2)

