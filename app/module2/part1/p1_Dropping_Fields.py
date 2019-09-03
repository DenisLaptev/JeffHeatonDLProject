import os
import pandas as pd

'''
Some fields are of no value to the neural network and can be dropped. 
'''

URL = "https://data.heatonresearch.com/data/t81-558/auto-mpg.csv"

# The following code removes the name column from the MPG dataset.

df = pd.read_csv(URL, na_values=['NA', '?'])

print(f"Before drop: {list(df.columns)}")
df.drop('name', 1, inplace=True)
print(f"After drop: {list(df.columns)}")
