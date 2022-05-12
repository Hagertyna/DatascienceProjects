import pandas as pd
import numpy as np
pd.DataFrame.to_csv?
data = pd.read_csv('missing_file.csv')
data
data.to_csv('new_missing.csv')
data.to_excel('new_missingexcel.xlsx',encoding = 'utf-8')
data.to_csv('new_sep.csv',sep ='|')
!type new_sep.csv
