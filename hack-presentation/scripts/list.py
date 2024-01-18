#!/usr/bin/env python3

thislist = ["apple", "banana", "cherry"]
print(thislist)

#the list() constructor
thislist = list(("apple", "banana", "cherry"))
print(thislist)
thislist = list("cherry")
print(thislist)


# access by index (Access Items)
print(thislist[1])

"""
Negative Indexing,
means beginning from the end,
-1 refers to the last item,
-2 refers to the second last item
"""
print(thislist[-1])

"""
Range of Indexes [start, end]
You can specify a range of indexes by
specifying where to start and
where to end the range
"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])
print(thislist[3:6])

"""
Change Item Value
To change the value of
 a specific item, refer to the index number
"""

thislist[1] = "blackcurrant"
print(thislist)
thislist[7:10] = "", "", "", ""
print(thislist)

#List Length
print(len(thislist))

"""
Add Items
"""
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# remove item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

thislist = ["apple", "banana", "cherry"]
t = thislist
t.remove("banana")
print(thislist)

#exist item (by in operator)
"apple" in thislist

# Copy a List
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Join Two Lists
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

# count of value
thislist = ["apple", "banana", "cherry", "banana"]
print(thislist.count("banana"))

# index of value
thislist = ["apple", "banana", "cherry", "banana"]
print(thislist.index("banana"))

# Reverses the order of the list
thislist = ["apple", "banana", "cherry"]
thislist.reverse()
print(thislist)
thislist.reverse()
print(thislist)

#sorts the list
thislist = ["apple",1,"s","A", "a", "banana", "cherry"]
thislist.sort()
print(thislist)
#TypeError: '<' not supported between instances of 'int' and 'str'

thislist = ["apple","s",'A', "a", "banana", "cherry"]
thislist.sort()
print(thislist)










