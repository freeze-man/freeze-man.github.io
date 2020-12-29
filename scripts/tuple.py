#!/usr/bin/env python3

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#the tuple() constructor
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

"""
Access Tuple Items
You can access tuple items by referring
to the index number, inside square brackets
"""

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

"""
Negative Indexing
means beginning from the end,
-1 refers to the last item,
-2 refers to the second last item etc
"""
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#Change Tuple Values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Tuple Length

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#Add Items (Error)
thistuple = ("apple", "banana", "cherry")
thistuple[3] = "orange" # This will raise an error
print(thistuple)

# remove with error
thistuple = ("apple", "banana", "cherry")
del thistuple
"""
this will raise an error because the
tuple no longer exists
"""
print(thistuple)
del thistuple[3]

#exist item (by in operator)
"apple" in thistuple

#all index is int not str (error)
thistuple["1"]

#Create Tuple With One Item
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#count of value

thistuple = ("apple", "banana", "banana", "cherry")
print(thistuple.count("banana"))

#index of value

thistuple = ("apple", "banana", "banana", "cherry")
print(thistuple.index("banana"))












