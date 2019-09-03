import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Creating a Series by passing a list of values, letting pandas create a default integer index:
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

print('------------------------------------------------')

# Creating a DataFrame by passing a numpy array, with a datetime index and labeled columns:
dates = pd.date_range('20130101', periods=6)
print(dates)

print('------------------------------------------------')

df1 = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df1)

print('------------------------------------------------')

# Creating a DataFrame by passing a dict of objects that can be converted to series-like
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print(df2)

print('------------------------------------------------')

print(df2.dtypes)

print('------------------------------------------------')

# See the top & bottom rows of the frame
print(df2.head())

print('------------------------------------------------')

print(df2.tail(3))

print('------------------------------------------------')

# Display the index, columns, and the underlying numpy data
print(df2.index)
print(df2.columns)
print(df2.values)

print('------------------------------------------------')

# Describe shows a quick statistic summary of your data
print(df1.describe())

print('------------------------------------------------')

# Transposing your data
print(df1.T)

print('------------------------------------------------')

# Sorting by an axis (сортирует по первому ряду по убыванию D,C,B,A)
print(df1.sort_index(axis=1, ascending=False))

print('------------------------------------------------')

# Sorting by values (сортирует по значениям в колонке B)
print(df1.sort_values(by='B'))

print('------------------------------------------------')

# Selecting a single column, which yields a Series, equivalent to df.A
print(df1['A'])

print('------------------------------------------------')

# Selecting via [], which slices the rows.
print(df1[0:3])

print('------------------------------------------------')

print(df1['20130102':'20130104'])

print('------------------------------------------------')

# Selection by Label
print(df1.loc[dates[0]])
print()
print()
print(df1.loc[:, ['A', 'B']])
print()
print()
print(df1.loc['20130102':'20130104', ['A', 'B']])
print()
print()
print(df1.loc['20130102', ['A', 'B']])
print()
print()
print(df1.loc[dates[0], 'A'])
print()
print()
print(df1.at[dates[0], 'A'])
print()
print()

print('------------------------------------------------')

# Selection by Position\
print(df1.iloc[3])
print()
print()
print(df1.iloc[3:5, 0:2])
print()
print()
print(df1.iloc[[1, 2, 4], [0, 2]])
print()
print()
# slicing rows/columns explicitly
print(df1.iloc[1:3, :])
print()
print()
print(df1.iloc[:, 1:3])
print()
print()
print(df1.iloc[1, 1])
print()
print()
print(df1.iat[1, 1])
print()
print()
print('------------------------------------------------')

# Boolean Indexing
print(df1[df1.A > 0])
print()
print()
print(df1[df1 > 0])
print()
print()
print('------------------------------------------------')
# Writing to a csv file
df1.to_csv('foo.csv')

# Reading from a csv file
text = pd.read_csv('foo.csv')
print(text)

print('------------------------------------------------')
# Writing to a HDF5 Store
df1.to_hdf('foo.h5','df')

# Reading from a HDF5 Store
text = pd.read_hdf('foo.h5','df')
print(text)

print('------------------------------------------------')
print('------------------------------------------------')
print('------------------------------------------------')
print('------------------------------------------------')
print('------------------------------------------------')
print('------------------------------------------------')
print('------------------------------------------------')
