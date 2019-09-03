import os
import pandas as pd
import numpy as np

'''
 The following code performs a shuffle and then saves a new copy.
'''

URL = "https://data.heatonresearch.com/data/t81-558/auto-mpg.csv"
path_to_folder = "."

df = pd.read_csv(URL, na_values=['NA', '?'])

filename_write = os.path.join(path_to_folder, "auto-mpg-shuffle.csv")

# Shuffling
df = df.reindex(np.random.permutation(df.index))

# write to csv-file
df.to_csv(filename_write, index=False)  # Specify index = false to not write row numbers
print("Done")
