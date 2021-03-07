thistuple = ("apple", "banana", "cherry")
print(thistuple)

type(thistuple)

l = list(thistuple)
s = set(thistuple)

type(l)
type(s)

print(thistuple[0])
print(thistuple[1])
print(thistuple[2])
print(thistuple["2"])

# print(thistuple[3])

thistuple[2] = ("apple") # non mutable, error
thislist = list(thistuple)
thislist[2] = ("apple")
thistuple = tuple(thislist)
print(thistuple)

print(thistuple[-1])
print(thistuple[-3])

print(thistuple[1: 2])
print(thistuple[0: 3])
print(thistuple[1:])
print(thistuple[:3])
print(thistuple[:-1])

print(thistuple[2:]) #note: one element, single item
testTuple = ("cherry")
print(testTuple)
type(testTuple)
testTuple = ("cherry",)
print(testTuple)
type(testTuple)

type(thistuple[1: 2])
type(thistuple[-3])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4: -1])
print(thistuple[3: 6])
print(thistuple[3: -1])
print(thistuple[3: 0])
print(thistuple[:])
print(thistuple[::])
print(thistuple[::1])
print(thistuple[::2])
print(thistuple[::-1])
print(thistuple[::-2])

print(len(thistuple))

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


a, b, c = thistuple
print(a, b, c)

t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)

t3.count(1)
t3 += t1
print(t3)
t3.count(1)

t3.index(5) # index of first find element
t3.index(1,2)
t3.index(1,3,6)
t3.index(5,4,6)



