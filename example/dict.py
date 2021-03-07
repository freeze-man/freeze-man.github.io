thisdict = {
	"brand": "Ford",
	"model": "Mustang",
	"year" : 1964
}

print(thisdict)
type(thisdict)

l = list(thisdict)
t = tuple(thisdict)
s = set(thisdict)

thislist = ["a1", "b2", "c3"]
d = dict(thislist)

dictTemp = dict(brand="Ford", model="Mustang", year=1964) # constrator
print(dictTemp)

print(thisdict["brand"])
print(thisdict.get("brand"))
print(thisdict.get("ban"))
print(thisdict["ban"])
print(thisdict.get("Engin", "Not Exist Info"))
print(thisdict.get("brand", "Not Exist Info"))

thisdict["brand"] = "Benz"
print(thisdict)

v = thisdict.values() # list of values's dict : type->dict_values
v[0]
print(v)
v = list(thisdict.values())
print(v)
v[0]

k = thisdict.keys() # list of keys's dict : type->dict_keys
k[0]
print(k)
k = list(thisdict.keys())
print(k)
k[0]

i = thisdict.items() # list of items's dict : type->dict_items
i[0]
print(i)
i = list(thisdict.items())
print(i)
i[0]


# for in  dict_values and dict_keys and dict_items
for x in thisdict.values():
	print(x)

for x in thisdict.keys():
	print(x)

for x, y in thisdict.items():
	print(x, y)

d = {"list": [1, 2, 3], "tuple": (4, 5, 6)}
d["list"]
type(d["list"])

d = {"list": [1, 2, 3], "tuple": (4, 5, 6), 1: "is number", 1.1: "is float"}
print(d[1])
print(d[1.1])

d[1.1] = 2.2
print(d[1.1])

# join dict or change
d.update({12: "12", 13: "13", 14: "14"})
print(d)
d.update({1.1: "is float"})
print(d)

d = d + {"15": 15} # error

13 in d
"color" in d

for x in d: # loop in keys (not enythings)
	print(d[x])


#for remove
p = d.pop(1.1) # any locat
print(d)
print(p)
d.update({1.1: "is float"})
print(d)
del d[1.1]
print(d)

d.clear()
print(d)


d = {"list": [1, 2, 3], "tuple": (4, 5, 6), 1: "is number", 1.1: "is float"}
d.popitem() #remove item from end of dict

# copy and clone new
dtemp = d
del d
print(dtemp)

d = dtemp.copy()
d2 = dict(d) #constructor

d3 = {}
d3[1] = "f1"
d3[2] = "f2"

d4 = dict()
d4[1] = "f1"
d4[2] = "f2"

#syntax
#nested_dict = { 'dictA': {'key_1': 'value_1'},
#                'dictB': {'key_2': 'value_2'}}

people = {1: {'name': 'John', 'age': '27'},
          2: {'name': 'Marie', 'age': '22'}}

print(people[1]['name'])
print(people[1]['age'])

people = {1: {'name': 'John', 'age': '27'},
          2: {'name': 'Marie', 'age': '22'}}

people[3] = {} # note you should be define first step

people[3]['name'] = 'Luna'
people[3]['age'] = '24'
people[3]['married'] = 'No'

print(people[3])

print(d)
d.update({"dict": {"a": "a", "b": "b"}})
print(d["dict"]["a"])

d1 = {'name': 'John', 'age': '27'}
d2 = {'name': 'Marie', 'age': '22'}
people = {1: d1,
          2: d2}
print(people)
# join (Merge dictionaries) with address
dic1 = {'men': 6, 'boy': 5}
dic2 = {'boy': 3, 'girl': 5}
merged_dic = {**dic1, **dic2}
print(merged_dic)


#dict comprehension/Derivation
test_dict = {i: i * i for i in range(10)}
print(test_dict)
#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}


