import os
import pandas as pd
import numpy as np
import pickle

'''
Pickling/unpickling is alternatively known as “serialization”, “marshalling,” “flattening”

 The pickle module implements binary protocols for serializing and de-serializing 
 a Python object structure. “Pickling” is the process whereby a Python object hierarchy is
 converted into a byte stream, and “unpickling” is the inverse operation, 
 whereby a byte stream (from a binary file or bytes-like object) 
 is converted back into an object hierarchy. 
 '''

URL = "https://data.heatonresearch.com/data/t81-558/auto-mpg.csv"
path_to_folder = "."

df = pd.read_csv(URL, na_values=['NA', '?'])

filename_write = os.path.join(path_to_folder, "auto-mpg-shuffle.pkl")

# Shuffling
df = df.reindex(np.random.permutation(df.index))

# write to pkl-file
with open(filename_write, "wb") as fp:
    pickle.dump(df, fp)

print("Done")
