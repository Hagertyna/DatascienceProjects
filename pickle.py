import pickle
clothes = {"shirt": ["red", "M"], "sweater": ["yellow", "L"], "jacket": ["black", "L"]}
clothes
#change into byte stream
pickle.dump(clothes,open(".clothes.pkl","wb")
#read the pickled data
with open(".clothes.pkl","rb") as f:
            unpickled = pickle.load(f)
print(unpickled)
            
