#!/usr/bin/env python3

# global
x = "global"
def foo():
 print("x inside:", x)

foo()
print("x outside:", x)

# local
def foo():
 y = "local"
 print(y)

foo()


### NameError: name 'y' is not defined
def foo():
 y = "local"

foo()
print(y)

### UnboundLocalError: local variable 'x'
### referenced before assignment
x = "global"

def foo():
 x = x * 2
 print(x)
foo()

# use global
x = "global"

def foo():
 global x
 y = "local"
 x = x * 2
 print(x)
 print(y)
 
foo()

# Global variable and Local variable with same name
x = 5
def foo():
 x = 10
 print("local x:", x)

foo()
print("global x:", x)

# nonlocal
#############1
def outer():
	x = "local"
	def inner():
		nonlocal x
		x = "nonlocal"
		print("inner:", x)
	inner()
	print("outer:", x)

outer()
#############2
def myfunc1():
  x = "John"
  def myfunc2():
    x = "hello"
  myfunc2()
  return x

print(myfunc1())
##############3
def myfunc1():
  x = "John"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

