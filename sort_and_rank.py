import pandas as pd
import numpy as np
series = pd.Series(range(6),index=['d','a','b','c','e','f'])
series
series.sort_index(axis=0,level=None, ascending=True)
df9 = pd.DataFrame(np.random.randn(4,5),
columns=list('bdeac'),index=['1','3','2','4'])
df9
df9.sort_index(axis=1,level=None,ascending=True)
df9.sort_index(axis=1,level=None,ascending=False)

df9.sort_index(axis=0,level=None,ascending=True)

df10=pd.DataFrame(np.arange(12).reshape((3,4)),
                 index=['1','2','3'],
                 columns=['d','a','b','c'])
df10
df10.sort_index(axis='index',level=None,ascending=True)

df10.sort_index(axis='index',level=None,ascending=False)

pd.DataFrame.sort_values?
df10.sort_index(axis='columns',level=None,ascending=True)

df9.sort_values(by=['b'])

df9.sort_values(by=['d'])
df9.rank()
df9.rank(axis='columns')
s= df9.loc[:,'b']
print(s)
s.rank()
