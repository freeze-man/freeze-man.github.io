#!/usr/bin/env python3

#global
x = "global"

def foo():
	print("x inside:", x)

#foo()
#print("x outside:", x)

""" Error
def foo0():
        x = x * 2
        print(x)

foo0()
"""

def foo1():
	y = "local"
	y = y * 2
	print(y)

#foo1()
#print("x outside:", x)
#print("y:", y)

#print("before x:", x)
def foo3():
	global x
	x = "local"
	x= x * 2

#foo3()
#print("after x:", x)


def foo4():
	x = "local"
	print("local x:", x)

#foo4()
#print("global x:", x)


def outer():
	global x
	x  = "local"
	def inner():
		#nonlocal x
		global x
		x = "nonlocal"
		print("inner:", x)
	inner()
	print("outer:", x)

outer()
#inner() # Error: NameError: name 'inner' is not defined
print("global x:", x)



