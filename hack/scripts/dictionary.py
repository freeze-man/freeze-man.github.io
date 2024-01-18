#!/usr/bin/env python3

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# The dict() Constructor

thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)

"""
Access Tuple Items
You can access the items of a dictionary
by referring to its key name,
inside square brackets
"""

x = thisdict["model"]
print(x)

x = thisdict.get("model")

x = thisdict.get("model", "Not Exist")

# Change Values

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

# get values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.values()
for x in thisdict.values():
  print(x)

# get keys
thisdict.keys()
for x in thisdict.values():
  print(x)

# get Items(value and key)
# into list of tuples
thisdict.items()
for x, y in thisdict.items():
  print(x, y)

#Dictionary Length

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict))

#Add Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#Add Items or update specified key-value pairs
#or Join Two dict
#(by update)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"type": 2})

thisdict = {
   "brand": "Ford",
   "model": "Mustang",
   "year": 1964
}
otherdict = {
   "count": 12,
   "stock": True
}
thisdict.update(otherdict)
print(thisdict)


#exist item (by in operator)
"color" in thisdict

# Removing items
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
del thisdict["model"]
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

# Removing last item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

# Copy a Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

mydict = dict(thisdict)
print(mydict)

#Nested Dictionaries (like json)
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}













