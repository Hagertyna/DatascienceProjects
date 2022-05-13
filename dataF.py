import pandas as pd

data = {"col_1": [3, 2, 1, 0], "col_2": ["a", "b", "c", "d"]}
pd.DataFrame.from_dict(data)
pd.DataFrame.from_dict(data, orient="index")
pd.DataFrame.from_dict(data, orient="index", columns=["A", "B", "C", "D"])
clothes = {"shirt": ["red", "M"], "sweater": ["yellow", "L"], "jacket": ["black", "L"]}
clothes_pd =pd.DataFrame.from_dict(clothes, orient="index",columns=["color","size"])
clothes_pd
#
info = """{
    "firstName": "Jallene",
    "lastName": "Dawit",
    "hobby": "scripting",
    "age": 35
}"""
print(info)
import json

data = json.loads(info)
data
data["firstName"]
df = pd.DataFrame.from_dict(data, orient="index", columns=["subject 1"])
print(df)

clothes = """{"shirt": ["red","M"], "sweater": ["yellow","L"]}"""
#data =pd.DataFrame.from_dict(clothes,orient="index",columns=["color","size"])
df = json.loads(clothes)
print(df)
