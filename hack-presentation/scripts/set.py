#!/usr/bin/env python3

thisset = {"apple", "banana", "cherry"}
print(thisset)

# The set() Constructor
thisset = set(("apple", "banana", "cherry")) 
# note the double round-brackets
print(thisset)

"""
Access Tuple Items
You cannot access items in a set by referring
to an index, since sets
are unordered the items has no index
"""

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}

#exist item (by in operator)
print("banana" in thisset)

# Change Items
"""
Once a set is created,
you cannot change its items,
but you can add new items.
"""
#set Length
thisset = {"apple", "banana", "cherry"}
print(len(thisset)

#Add Items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange") #To add one item
print(thisset)
thisset.update(["orange", "mango", "grapes"]) #To add more than one item
print(thisset)

# Removing items
"""
Note: If the item to remove does not exist
remove() will raise an error
"""
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

"""
Note: If the item to remove does not exist,
discard() will NOT raise an error
"""
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

"""
You can also use the pop(),
method to remove an item,
but this method will remove the last item.
Remember that sets are unordered,
so you will not know what item that gets removed
"""
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

"""
removing all items by clear method
"""
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

"""
delete the set completely
"""
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

# Join Two Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set1 | set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# Copy a set
thisset = {"apple", "banana", "cherry"}
otherset = thisset.copy()
print(otherset)

# Difference between two or more sets
# persian(azaee ke moshtarak nist az majmoe)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)
print(x - y)
z = y.difference(x)
print(z)

# Remove the items that exist in both sets
# and stay difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)

# The returned set contains only items that exist in both sets
# (persian) eshterak
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(x & y)
print(z)

# Remove the items that is not present in both x, and set y
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

# Return True if no items in set x is present in set y
# (persian) eshterak nadarad is True
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)

# Returns whether another set contains this set or not
# (persian) zir majmoe has ya na
# (persian) x zir majmoe y hast ya na
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

# Return True if all items set y are present in set x
# (persian) y zir majmoe x hast ya na
# (persian) x majmoe kol ya marja hast ya na
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)

# Returns a set with the symmetric differences of two sets
# Return a set that contains all items from both sets,
# except items that are present in both sets
# (persian) hame ozvha begher(bejoz) 
# az eshterak
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
print(x ^ y)

# Remove the items that are present in both sets,
# AND insert the items that is not present in both sets.
# inserts the symmetric differences from this set and another
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)






