#import
import pandas as pd
import numpy as np
data = pd.Series(np.arange(6),index=['a','b','c','d','e','f'])
print(data)
n_data = data.drop('a')
n_data
data.drop(['a','d'])
dataf= pd.DataFrame(np.arange(16).reshape(4,4),
index=['a','b','e','f'],columns=['Addis Ababa','Hawassa','Dire','Sheger'])
print(dataf)
dataf.drop(['a','e'])
dataf.drop(['Sheger'],axis=1)
# gives us original data since implace is equaltoFalse by default in grop method
print(dataf)
new_dat =dataf.drop('Dire',axis = 1)
new_dat

#lets drop nan value lets say df dataframe
df.dropna(inplace=True)
