# Python Default Arguments

def greet(name, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """

    print("Hello", name + ', ' + msg)


greet("Kate")
greet("Bruce", "How do you do?")
#------------------
def outer():
	x = "local"
 
	def inner():
		nonlocal x
		x = "nonlocal"
		print("inner:", x)
 
	inner()
	print("outer:", x)

outer()
#>>> outer()
#inner: nonlocal
#outer: nonlocal

#------------------
x = "global"

def foo():
	global x
	y = "local"
	x = x * 2
	print(x)
	print(y)

foo()
print(x)

#>>> foo()
#globalglobal
#local
#>>> print(x)
#globalglobal

#------------------
x = 0
def foo():
    x = 20
    def bar():
        global x
        x = 25
    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)


foo()
print("x in main: ", x)

#>>> foo()
#Before calling bar:  20
#Calling bar now
#After calling bar:  20
#>>> print("x in main: ", x)
#x in main:  25

#------------------
#------------------
#------------------
#------------------
#------------------
#------------------
#------------------


