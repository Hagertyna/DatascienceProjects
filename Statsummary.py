import pandas as pd
import numpy as np
df = pd.DataFrame([[1.4, np.nan], [7.1,-4.5], [np.nan, np.nan], [0.75, -1.3]],
                  index=['a','b','c','d'],
                  columns=['one', 'two'])
print(df)
df.sum()
df.sum(axis='columns')
df.mean(axis='columns', skipna=False)
df.idxmax()
df.cumsum()
df.describe()
ser = pd.Series(['a','b','c','d']* 4)
print(ser)
print(ser.describe())
