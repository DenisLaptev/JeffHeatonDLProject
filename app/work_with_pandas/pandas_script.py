# Simple dataframe
import os
import pandas as pd

df = pd.read_csv("https://data.heatonresearch.com/data/t81-558/auto-mpg.csv")
print(df[0:5])

#-----------------------STATISTICS-----------------------


# Strip non-numerics
df = df.select_dtypes(include=['int', 'float'])

headers = list(df.columns.values)
fields = []

for field in headers:
    fields.append({
        'name' : field,
        'mean': df[field].mean(),
        'var': df[field].var(),
        'sdev': df[field].std()
    })

for field in fields:
    print(field)

df2 = pd.DataFrame(fields)
print(df2)
