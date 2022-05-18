import pandas as pd
df1 = pd.read_csv("data/mexico-real-estate-1.csv")
df2 = pd.read_csv("data/mexico-real-estate-2.csv")
df3 = pd.read_csv("data/mexico-real-estate-3.csv")
df1.info()
df1.head()
df1.shape
df1.dropna(inplace =True)
df1["price_usd"].head()
#remove$ sign and comma
df1["price_usd"].str.replace("$","",regex=False).str.replace(",","")
# transform its type from object to float
df1["price_usd"] =df1["price_usd"].str.replace("$","",regex=False).str.replace(",","").astype(float)

#df2
df2.info()
df2.head()
df2.shape
df2.dropna(inplace =True)
#use the "price_mxn" column to create a new column named "price_usd"
df2["price_usd"]=df2["price_mxn"]
print(df2["price_usd"])
#drop the "price_mxn" from the DataFrame.
df2 = df2.drop("price_mxn",axis= 'columns')
print(df2)

#clean df3
df3

df3.info()
df3.head()
df3.shape
df3.dropna(inplace =True)
#Here, expand is telling pandas to make the DataFrame bigger; 
#that is, to create a new column without dropping any of the ones that already exist.
##df3["lat","lon"]= df3["lat-lon"].str.split(",",expand= True)
df3[["lat", "lon"]] = df3["lat-lon"].str.split(",", expand=True)
#extracting
df3["place_with_parent_names"].str.split("|",expand= True)
#since we need the second column only which is state
df3["place_with_parent_names"].str.split("|",expand= True)[2]
#create state column from the second entry of place_with...
df3["state"] = df3["place_with_parent_names"].str.split("|",expand= True)[2]
#before droping
print(df3)
#drop columns
df3.drop(columns =["place_with_parent_names","lat-lon"], inplace=True)
#conncatinate the three dfr into one df 
df = pd.concat([df1,df2,df3])
#df.dropna(inplace = True)
print(df.shape)
df.head()
#save df
df.to_csv("./data/mexico-real-estate-clean.csv")
#clear index fromsaved data
# remove indexing since its default is true 
df.to_csv("./data/mexico-real-estate-clean.csv",index = False)
