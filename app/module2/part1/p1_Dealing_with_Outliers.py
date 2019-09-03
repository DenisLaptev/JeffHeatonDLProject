import pandas as pd
import os
import numpy as np
from sklearn import metrics
from scipy.stats import zscore

'''
Outliers are values that are unusually high or low. 
Sometimes outliers are simply errors, this is a result of observation error. 
Outliers can also be truly large or small values that may be difficult to account for. 
Outliers are usually defined as a value that is several standard deviations from the mean. 
'''

URL = "https://data.heatonresearch.com/data/t81-558/auto-mpg.csv"


# function to remove Outliers
# Remove all rows where the specified column is +/- number_of_sd standard deviations
def remove_outliers(df, name, number_of_sd):
    delta = np.abs(df[name] - df[name].mean())
    sd_error = number_of_sd * df[name].std()

    drop_rows = df.index[delta >= sd_error]
    df.drop(drop_rows, axis=0, inplace=True)


# create data frame
df = pd.read_csv(URL, na_values=['NA', '?'])

print(df[0:5])
print('-----------------------------------')
print()

# fill na values in the 'horsepower' column by median
med = df['horsepower'].median()
df['horsepower'] = df['horsepower'].fillna(med)

# drop the 'name' column from the table
df.drop('name', 1, inplace=True)

# drop outliers in 'horsepower' column
print("Length before MPG outliers dropped: {}".format(len(df)))
remove_outliers(df, 'mpg', 2)
print("Length after MPG outliers dropped: {}".format(len(df)))

print('-----------------------------------')
print()

print(df[0:5])
