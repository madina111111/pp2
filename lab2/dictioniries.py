thisdict = {
    "Brand": "Ford",
    "model": "Mustang",
    "year": "1995"
}
print(thisdict)

thisdict = {
    "Brand": "Ford",
    "model": "Mustang",
    "year": "1995"
}
print(thisdict["model"])

thisdict = {
    "Brand": "Ford",
    "model": "Mustang",
    "year": "1995"
}
x = thisdict["model"]
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

car["year"] = 2020
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

car["year"] = 2020

print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

car["color"] = "red"
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
if "model" in car:
    print("Yes, model is in car")

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
car["brand"] = "ferrari"
print(car)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
car.update({"year": 2020})
print(car)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
   print(x)

for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)

for x in thisdict.keys():
    print(x)

for x,y in thisdict.items():
    print(x,y)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

myFamily = {
    "child1": {
        "name" : "Emil",
        "year" : 2005
    },
    "child2": {
        "name" : "Tobias",
        "year" : 1998
    },
    "child3": {
        "name" : "Linus",
        "year": 2018
    }
}
print(myFamily)

child1 = {
    "name" : "Emil",
    "year" : "2005"
}
child2 = {
    "name" : "Tobias",
    "year" : "1998"
}
child3 = {
    "name" : "Linus",
    "year" : 2005
}

myFamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}
print(myFamily)

print(myFamily["child1"]["name"])

