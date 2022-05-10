import pandas as pd
import numpy as np

data_sr = pd.read_csv('skip_rows.csv',skiprows=[0,2,8])
data_sr

!type missing_file.csv
missing_d = pd.read_csv('missing_file.csv')
missing_d
missing_d.isnull()
