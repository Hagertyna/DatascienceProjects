import pandas as pd
import numpy as np
#pd.read_csv?
!type ex1.csv
data = pd.read_csv('ex1.csv')
data
data_d = pd.read_csv('ex2.csv',header=None)
print(data_d)
data_d = pd.read_csv('ex2.csv',header=None, names=['N1','N2','N3','Prog_name'])
data_d
#assign row and columns label
names_index =['N1','N2','N3','Prog_name']
data_c = pd.read_csv('ex2.csv',header=None, names=names_index, index_col="Prog_name")
data_c
#lets see data type of our file
!type hindex.csv
data_hind = pd.read_csv('hindex.csv',index_col =['cat','type'])
data_hind
