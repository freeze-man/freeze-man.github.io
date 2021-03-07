#!/usr/bin/env python3
#https://www.programiz.com/python-programming/decorator
#https://realpython.com/primer-on-python-decorators/

def first(msg):
    print(msg)


first("Hello")

second = first
second("Hello")

#---------#

def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operate(func, x):
    result = func(x)
    return result

operate(inc,3) #->4
operate(dec,3) #->2
#---------#

def is_called():
    def is_returned():
        print("Hello")
    return is_returned


new = is_called()

# Outputs "Hello"
new()

#---------#

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")

ordinary()
#I am ordinary

# let's decorate this ordinary function
pretty = make_pretty(ordinary)
pretty()
#I got decorated
#I am ordinary

#--------#

@make_pretty
def ordinary():
    print("I am ordinary")
#->is equivalent to
def ordinary():
    print("I am ordinary")
ordinary = make_pretty(ordinary)

#--------#

def divide(a, b):
    return a/b

divide(2,5) #=>0.4
divide(2,0) #=>ZeroDivisionError: division by zero


#----For More Info----#
def works_for_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)
    return inner

#Chaining Decorators in Python
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Hello")
#******************************
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#Hello
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#******************************
#->is equivalent to
def printer(msg):
    print(msg)
printer = star(percent(printer))
printer("Hello")
