newcars = {
    "brand": "BMW",
    "model": "X5",
    "year": 2022
}

print(newcars)
type(newcars)
print(newcars["brand"])
x = newcars.get("brand")
print(x)
len(newcars)
#print keys
x = newcars.keys()
print(x)
newcars["color"] = "black"
print(newcars)

car = newcars.values()
print(car)
newcars["year"] = 2019
print(newcars)
items = newcar.items()
print(items)
if "color" in newcars:
    print("Yes, color is in newcars!")
newcars.pop("year")
print(newcars)
if "color" in newcars:
    print("Yes, color is in newcars!")
newcars.update({"color": "white"})
print(newcars)
