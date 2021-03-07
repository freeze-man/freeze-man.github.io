#!/usr/bin/env python3

def greet1(name, msg):
    """This function greets to the person with the provided message"""
    print("Hello", name + "," + msg)

# greet1("Monica", "Good morning!")

def first(msg):
    print(msg)


first("Hello")

second = first
#second("Hello")


def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()

#parent()

def is_called():
    def is_returned():
        print("Hello")
    return is_returned

new = is_called()
#new()
# Outputs "Hello"

def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operate(func, x):
    result = func(x)
    return result

#operate(inc,3)
# output : 4
#operate(dec,3)
# output : 2

def greet2(name, msg="Good morning!"):
    """This function greets to the person with the provided message"""
    print("Hello", name + "," + msg)

#greet2("Monica")
#greet2("FreezeMan", "Come On!!!")
#greet2("FreezeMan", msg="Come On!!!")
#greet2(msg="Come On!!!", "FreezeMan") # Error(SyntaxError: positional argument follows keyword argument)
#greet2(msg="Come On!!!", name="FreezeMan")
#greet2(name="FreezeMan", msg="Good morning !!!")
#greet2(name="FreezeMan", msg="Good morning !!!", "asdasd") # Error SyntaxError: positional argument follows keyword argument


def greet3(name="Monica", msg):
       """SyntaxError: non-default argument follows default argument"""
       print("Hello", name + "," + msg)


def my_sum(*args):
    result = 0

    print("args: ", type(args))
    if args and args[0]:
        print(args[0])
    for x in args:
        result += x
    return result

#print(my_sum(1 ,2, 3))
#print("-----------")
#print(my_sum())
#print("-----------")
#print( my_sum( (1 ,2, 3) ) ) # Error
#print(my_sum(*(1,2,3)))

def greet(*names):
    """This function greets all
    the person in the names tuple."""
    print("hello", names)
    # names is a tuple with arguments
    for name in names:
        print("Hello", name)
    print("Hello", name[0])
    print("Hello", names[1])
    print("Hello", names[2])
    print("Hello", names[3])


greet("Monica", "Luke", "Steve", "John")
#Hello Monica
#Hello Luke
#Hello Steve
#Hello John


# A function that takes dictionary 
# as an argument 
def func(d): 
      
    for key in d: 
        print("key:", key, "Value:", d[key]) 
          
# Driver's code 
D = {'a':1, 'b':2, 'c':3} 
func(D)
####Output:####
#key: b Value: 2
#key: a Value: 1
#key: c Value: 3


# Python program to demonstrate 
# passing dictionary as kwargs 
def display(**name): 
      
    print (name["fname"]+" "+name["mname"]+" "+name["lname"]) 
  
def main(): 
      
    # passing dictionary key-value  
    # pair as arguments 
    display(fname ="John", 
            mname ="F.",  
            lname ="Kennedy") 
# Driver's code 
main()

####Output:####
#John F. Kennedy


# Python program to demonstrate 
# passing dictionary as kwargs
def display(x = 0, y = 0, **name): 
      
    print (name["fname"]+" "+name["mname"]+" "+name["lname"]) 
    print ("x =", x) 
    print ("y =", y) 
  
def main(): 
    # passing dictionary key-value  
    # pair with other arguments 
    display(2, fname ="John", mname ="F.", lname ="Kennedy") 
      
# Driver's code 
main() 

####Output:####

#John F. Kennedy
#x = 2
#y = 0

def concatenate(**kwargs):
    result = ""

    for x, y in kwargs:
        print(x, y)
    for arg in kwargs.values():
	result += arg
    for key in kwargs.keys():
	print(key)
    return result

#print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))

def my_function(a, b, *args, **kwargs):
    print("a =", a)
    print("b =", b)
    print("args =", args)
    print("kwargs =", kwargs)

#my_function(1,2)
#print("-----------")
#my_function(1,2,3,4)
#print("-----------")
#my_function(1,2,3,4,5, name="FreezeMan")
