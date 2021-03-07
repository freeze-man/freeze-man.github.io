thislist = ["apple", "banana", "cherry"]
print(thislist)
type(thislist)

t = tuple(thislist)
s = set(thislist)

type(t)
type(s)

thislist[2] = ["apple"] # mutable
thislist[3] = ["test"] #error, for append or insert item exist function
thislist = ["apple"] # can define single item

print(thislist[0])
print(thislist[1])
print(thislist[2])
print(thislist["2"])

# print(thislist[3])

print(thislist[-1])
print(thislist[-3])

print(thislist[1: 2])
print(thislist[0: 3])
print(thislist[1:])
print(thislist[:3])
print(thislist[:-1])

type(thislist[1: 2])
type(thislist[-3])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4: -1])
print(thislist[3: 6])
print(thislist[3: -1])
print(thislist[3: 0])
print(thislist[:])
print(thislist[::])
print(thislist[::-1])
print(thislist[::-2])
print(thislist[::1])
print(thislist[::2])
print(thislist[::2])

thislist[7:] = "", "", "", "test"
print(thislist)
thislist[7:] = "", "", "", "change test"
print(thislist)


list = [1, 'python', 3]
print(list)
#[1, 'python', 3]
a, b, c = list 
print(a, b, c)
#1 python 3


print(len(thislist))

thislist = ["apple", "banana", "cherry"]

print(len(thislist))

# a[len(a):] = [x]
thislist.append("orange") # end of list added -> thislist[3] = "orange" check error

thislist[3:] = "orange"
print(thislist)
thislist[3:] = ["orange"]
print(thislist)
thislist[0:2] = [1, 12]
print(thislist)
thislist[0:2] = 41, 127
print(thislist)

thislist = thislist + [12,22]
print(thislist)
thislist = 3 * thislist[:3] + ['Boe!']
print(thislist)

thislist[1] = thislist[1] + 23
print(thislist)


print(thislist)
thislist.insert(1, "melon")
thislist.insert(1, "orange")
print(thislist)

thislist[1:1] = [’bletch’, ’xyzzy’]
print(thislist)
thislist[:0] = thislist
print(thislist)

thislist.remove("banana")
print(thislist)
thislist.remove("orange")
thislist.remove("orange") # ValueError
print(thislist)

thislist.pop() # output element | end of list
print(thislist)

del thislist[2]
print(thislist)

thislist[0:2] = []
print(thislist)

thislist.clear() # empty list all element


thislist = ["apple", "banana", "cherry"]
l = thislist # reffer by address
l.remove("banana")
print(thislist)
print(l)
# for append, pop, insert too this event

#but follow diffrent clone method
thislist = ["apple", "banana", "cherry"]
#a[:]
l = thislist.copy()
print(thislist)
print(l)
l.remove("banana")
print(thislist)
print(l)
#constractor
thislist = ["apple", "banana", "cherry"]
l = list(thislist)
print(thislist)
print(l)
l.remove("banana")
print(thislist)
print(l)

"apple" in l
"banana" in l

l3 = l + thislist
print(l3)

del l3

# a[len(a):] = iterable
thislist.extend(l)
print(thislist)


l.count("apple") # count of repeat element

l.index("apple") # index of first find element
l.index("banana") # ValueError
l.index("apple", 0, 1)

l.reverse()
print(l)
l.reverse()
print(l)

l.sort() # ascii code sorted Ali=>1 ALi=>2 AlI=>3
list_unsort = ["Ali", "ALi", "AlI"]
print(l)

l.sort(key=None,reverse=False)

l.reverse()
print(l)
l.sort()
print(l)

l.append(3)
l.sort()

# using slicing approach
def Reverse(lst): 
 lst1 = lst[::-1] 
 return lst1
 
lst = [5, 6, 7, 8, 9, 10] 
print(Reverse(lst))


# Multiplying each item in the list with 3
list1 = [2,4,6,8]
list2 = [3*p for p in list1]
print(list2)
#[6,12,18,24]


#list comprehension/Derivation
list = [m**2 if m>5 else m**4 for m in range(10)]
print(list)
#[0, 1, 16, 81, 256, 625, 36, 49, 64, 81]

squares = []
for x in range(10):
    squares.append(x**2)

squares = [x**2 for x in range(10)]


squares = list(map(lambda x: x**2, range(10)))

combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))


vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
testList = [x*2 for x in vec]
#[-8, -4, 0, 4, 8]
# filter the list to exclude negative numbers
testList = [x for x in vec if x >= 0]
#[0, 2, 4]
# apply a function to all the elements
testList = [abs(x) for x in vec]
#[4, 2, 0, 2, 4]
# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
testList = [weapon.strip() for weapon in freshfruit]
#['banana', 'loganberry', 'passion fruit']
# create a list of 2-tuples like (number, square)
testList = [(x, x**2) for x in range(6)]
#[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
testList = [num for elem in vec for num in elem]
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

testList = [[row[i] for row in matrix] for i in range(4)]
#[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

testList = []
for i in range(4):
    testList.append([row[i] for row in matrix])


testList = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
        testList.append(transposed_row)


#Here is the code that uses map(), list comprehension, and a simpler approach for digitizing
number = 2468 #=>[2468]
# with map
digit_list = list(map(int, str(number)))
print(digit_list)
[2, 4, 6, 8]
# with list comprehension
digit_list = [int(a) for a in str(number)]
print(digit_list)
[2, 4, 6, 8]
# Even simpler approach
digit_list = list(str(number))
print(digit_list)
[2, 4, 6, 8]



#Using enumerators, finding an index is quick when you’re within a loop.
sample_list = [4, 5, 6]
for j, item in enumerate(sample_list):
	print(j, ': ', item)


#Create Python List Use itertools Module.
import itertools
 
test = [['java', 'python'], ['ford', 'bmw'], [25, 35]]
it = itertools.chain.from_iterable(test)
print(it)
#<itertools.chain object at 0x7f7322ee0d30>
list = list(it)
print(list)
#['java', 'python', 'ford', 'bmw', 25, 35]


from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
#'Eric'
queue.popleft()
#'John'


