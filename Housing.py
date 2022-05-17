import pandas as pd
# creating data frames
df1 = pd.read_csv("data/mexico-real-estate-1.csv")
df2 = pd.read_csv("data/mexico-real-estate-2.csv")
df3 = pd.read_csv("data/mexico-real-estate-3.csv")
#lets work on cleaning dataframe 1
df1.info()
df1.shape
df1.head()
#drop all datas with nan values using inplace true
df1.dropna(inplace =True)
#df1.info gives us 583 rows
df1.info()
df1["price_usd"].head()
#lets remove $ sign from price clumn and change it into float
df1["price_usd"].str.replace("$","",regex=False).str.replace(",","")
