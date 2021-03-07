thisset = {1, 2, 2, 3, 3, 3}
print(thisset)

thisset = {1, 2, 2, 3, "3", 3.3}
print(thisset)

for x in thisset:
	print(x)

1 in thisset

len(thisset)

thisset.add(4)
thisset.add("orange")
print(thisset)

thisset.remove("orange")
print(thisset)

thisset.discard("orange") # no error for not exist item

thisset.pop() # not ordered | not matter

thisset.clear() # remove all

del thisset

set_1 = {5, 89, 100, 9}
set_2 = {15, 9, 10, 100}

set_3 = set_1.union(set_2)
print(set_3)
set_3 = set_1 | set_2 # just union (اجتماع)
print(set_3)

set_3 = set_1.difference(set_2)
print(set_3)
set_3 = set_1.update(set_2) #remove exist both item (اختلاف از هم و مشترک حذف)
print(set_3)

set_3 = set_1.intersection(set_2)
print(set_3)
set_3 = set_1 & set_2 # just intersection (اشتراک)
print(set_3)
set_3 = set_1.intersection_update(set_2)
print(set_3)

set_1.isdisjoint(set_2) # آيا عضو مشترک دارد یا نه

set_1 = {5, 89, 100, 9}
set_2 = {15, 9, 10, 100, 89, 5}

set_1.issubset(set_2) # زیر مجموعه هست یا نه set_2

set_1.issuperset(set_2) # زیر مجموعه کامل هست یا نه set_2

set_1.symetric_difference(set_2) #حذف اشتراک ها از دو مجموعه و گذاشتن باقی  عضو ها

set_3 = set_1.symetric_difference_update(set_2)

s = set_1
s.pop() # remove both
print(set_1)
print(s)

s = set_1.copy()
s.pop()
print(set_1)
print(s)

test_set = {i * 2 for i in range(10)}
print(test_set)
#{0, 2, 4, 6, 8, 10, 12, 14, 16, 18}

