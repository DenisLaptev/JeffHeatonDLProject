import os
import pandas as pd

'''
Можно составить (конкатенировать) новую таблицу из нескольких колонок старой.
Можно составить (конкатенировать) новую таблицу из нескольких рядов старой.
'''

URL = "https://data.heatonresearch.com/data/t81-558/auto-mpg.csv"

df = pd.read_csv(URL, na_values=['NA', '?'])

# получили 2 колонки ('horsepower', 'name') из старой таблицы
col_horsepower = df['horsepower']
col_name = df['name']

# составили (конкатенировали) новую таблицу из полученных столбцов
result_cols = pd.concat([col_name, col_horsepower], axis=1)
print(result_cols[0:5])

print('-----------------------------------')
print()

# составили (конкатенировали) новую таблицу из двух первых и двух последних строк
result_rows = pd.concat([df[0:2], df[-2:]], axis=0)
print(result_rows)
