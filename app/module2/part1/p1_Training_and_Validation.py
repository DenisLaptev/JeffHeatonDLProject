import os
import pandas as pd
import numpy as np

'''
The code below performs a split of the MPG data into a training(80%) and validation(20%) set. 
'''

URL = "https://data.heatonresearch.com/data/t81-558/auto-mpg.csv"

df = pd.read_csv(URL, na_values=['NA', '?'])

# Usually a good idea to shuffle
df = df.reindex(np.random.permutation(df.index))

mask = np.random.rand(len(df)) < 0.8

trainDF = pd.DataFrame(df[mask])
validationDF = pd.DataFrame(df[~mask])

print(f"Training DF: {len(trainDF)}")
print(f"Validation DF: {len(validationDF)}")
