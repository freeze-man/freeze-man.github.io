#!/usr/bin/env python3

#global
x = "global"

#----------------#
def foo():
    print("x inside: ", x)

foo()
#x outside: global

#----------------#
def foo0():
    x = x * 2
    print(x)

foo0()
#UnboundLocalError: local variable 'x' referenced before assignment

#----------------#
def foo1():
    y = "local"
    y = y * 2
    print(y)

foo1()
#locallocal
print("x outside: ", x) #=> x outside: global
print("y:", y) #=> NameError: name 'y' is not defined

#----------------#
def foo3():
    global x
    x = "local"
    x= x * 2

print("before x: ", x) #=> before x: global
foo3()
print("after x: ", x) #=> after x: locallocal

#----------------#
def foo4():
    x = "local"
    print("local x: ", x)

#foo4()
#local x: local
print("global x: ", x) #=> global x: locallocal

#----------------#
x = "global"
#----------------#
def outer():
    x = "local in func outer"

    def inner():
        x = "local in inner"
        print("inner: ", x)
    inner()
    print("outer: ", x)

outer()
#inner: local in inner
#outer: local in func outer
print("global x: ", x)
#global x: global

#----------------#
def outer():
    x  = "local"
    def inner():
	nonlocal x 
	x = "nonlocal"
	print("inner: ", x)
    inner()
    print("outer: ", x)

outer()
#inner: nonlocal in inner
#outer: nonlocal in inner
print("global x: ", x)
#global x: global

#----------------#
def outer():
    global x
    x  = "local"
    def inner():
	nonlocal x # Error
	x = "nonlocal"
	print("inner: ", x)
    inner()
    print("outer: ", x)

outer()
#SyntaxError: no binding for nonlocal 'x' found

#----------------#
def outer():
    global x
    x = "local in func outer"

    def inner():
        global x
        x = "nonlocal in inner"
        print("inner: ", x)
    inner()
    print("outer: ", x)

outer()
#inner: nonlocal in inner
#outer: nonlocal in inner
print("global x: ", x)
#global x: nonlocal in inner

#----------------#
def outer():
    global x
    x = "local in func outer"

    def inner():
        x = "local in inner"
        print("inner: ", x)
    inner()
    print("outer: ", x)

outer()
#inner: local in inner
#outer: local in func outer
print("global x: ", x)
#global x: local in func outer

#----------------#
def outer():
    x = "local in outer"
    def inner():
        global x
        x = "local in inner"
        print("inner: ", x)
    inner()
    print("outer: ", x)


outer()
#inner: local in inner
#outer: local in outer
print("global x: ", x)
#global x: local in inner
#------------------
inner() # Error: NameError: name 'inner' is not defined



