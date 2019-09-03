import os
import pandas as pd
import numpy as np

'''
Neural networks do not directly operate on Python dataframes. 
A neural network requires a numeric matrix. 
The values property of a dataframe is used to convert to a matrix. 
'''

URL = "https://data.heatonresearch.com/data/t81-558/auto-mpg.csv"
df = pd.read_csv(URL, na_values=['NA', '?'])

print(df.values)

print('-----------------------------------')
print()

# to convert only some of the columns, (i.e without 'name' column), use the following code
print(df[['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
          'acceleration', 'year', 'origin']].values)
