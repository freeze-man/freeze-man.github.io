# -*- coding: utf-8 -*-

"""value swapping"""
a, b= 5, 10
print(a, b) 
a, b= b, a
print(a, b)

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)


check = (1, 2, 3) < (1, 2, 4)
check = 'ABC' < 'C' < 'Pascal' < 'Python'

# function returning several elements.
def a():
	return 5, 6, 7, 8
# Calling the above function.
w, x, y, z= a()
print(w, x, y, z)


# Incorporate a true Python switch-case statement
def aswitch(a): 
	return aswitch._system_dic.get(a, None)

aswitch._system_dic = {'mangoes': 4, 'apples': 6, 'oranges': 8}
print(aswitch('default'))
print(aswitch('oranges'))


# Find The Smallest Number In ABC
def smallest_value(a, b, c):
     return a if a<b and a<c else (b if b<a and b<c else c)
 
print(smallest_value(1, 0, 1))
#0
print(smallest_value(1, 0, 9))
#0
print(smallest_value(1, 2, 9))
#1


import os
print(os)
#<module 'os' from '/home/zhaosong/anaconda3/lib/python3.7/os.py'>



#Use dir() Method To Display All Methods And Attributes Of Python Object
list = ['java', 'python']
print(dir(list))
#['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


#help command | define function docstring
help()


import sys
print(hasattr(sys, "hexversion"))
# True
py_version = sys.version_info
print(py_version)
# sys.version_info(major=3, minor=6, micro=5, releaselevel='final', serial=0)
print(sys.version)
# '3.6.5 |Anaconda, Inc.| (default, Apr 26 2018, 08:42:37) \n[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)]'
print(sys.argv)
#['']

import os
print(os.environ['PATH'])
execfile(os.environ['PYTHONSTARTUP'])


#Define Enumerator
class colors:
     red, blue, green = range(3)

colors.red
# 0
colors.blue
# 1
colors.green
# 2



#Use * Operator To Unpack Function Parameters
def test_func(a, b, c):
     print(a)
     print(b)
     print(c)
 
test_dict = {'a':1, 'b':2, 'c':3}
test_list = ['java', 'python', 'c++']
test_func(*test_dict)
# a
# b
# c
test_func(**test_dict)
# 1
# 2
# 3
test_func(*test_list)
# java
# python
# c++



#Use Dictionary To Store Expressions
dict_lambda = {
    "add": lambda x, y: x + y,
    "multiple": lambda x, y: x * y
}
dict_lambda["add"](1, 1)
# 2
dict_lambda["multiple"](9, 3)
# 27



#Check An Object Used Memory Size
import sys
str_1 = 'python'
str_size = sys.getsizeof(str_1)
print(str_size)
# 55
print(str_1.__sizeof__())
# 55

###sorted
a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a)
print(x)

a = (1, 11, 2)
x = sorted(a)
print(x)

a = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(a, reverse=True)
print(x)

###reversed
alph = ["a", "b", "c", "d"]
ralph = reversed(alph)
for x in ralph:
  print(x)

seq_string = 'Python'
print(list(reversed(seq_string)))

seq_range = range(5, 9)
print(list(reversed(seq_range)))

###enumerate
grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery))

# converting to list
print(list(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))

grocery = ['bread', 'milk', 'butter']

for item in enumerate(grocery):
  print(item)

for count, item in enumerate(grocery):
  print(count, item)

###Output:

# <class 'enumerate'>
# [(0, 'bread'), (1, 'milk'), (2, 'butter')]
# [(10, 'bread'), (11, 'milk'), (12, 'butter')]
# (0, 'bread')
# (1, 'milk')
# (2, 'butter')
# 0 bread
# 1 milk
# 2 butter

###round
x = round(5.76543, 2)
print(x) 

print(round(5.76663, 0))

x = round(5.76543)
print(x)


###pow
#Return the value of 4 to the power of 3, modulus 5 (same as (4 * 4 * 4) % 5):
x = pow(4, 3, 5) 
print(x)

###max
x = max("Mike", "John", "Vicky")
print(x)
a = (1, 5, 3, 9)
x = max(a)
print(x)

###min
x = min("Mike", "John", "Vicky")
print(x)
a = (1, 5, 3, 9)
x = min(a)
print(x)

###abs
x = abs(-7.25)
print(x)

###sum
a = (1, 2, 3, 4, 5)
x = sum(a, 7)
print(x)

a = (1, 2, 3, 4, 5)
x = sum(a) 
print(x)



# "is" vs "=="
# • "is" expressions evaluate to True if two 
#   variables point to the same object

# • "==" evaluates to True if the objects 
#   referred to by the variables are equal

a = [1, 2, 3]
b = a

print(a is b) #True
print(a == b) #True

c = list(a)

print(a == c) #True
print(a is c) #False

