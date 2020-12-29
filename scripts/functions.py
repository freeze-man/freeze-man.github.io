#!/usr/bin/env python3

def absolute_value(num):
	"""This function returns the absolute
	value of the entered number (even numbers)"""
	if num >= 0:
		return num
	else:
		return -num

print(absolute_value(2))
print(absolute_value(-4))
print(absolute_value.__doc__)
######################
def my_func():
	x = 10
	print("Value inside function:",x)

x = 20
my_func()
print("Value outside function:",x)
######################
def greet(name, msg):
    """This function greets to
    the person with the provided message"""
    print("Hello", name + ', ' + msg)

greet("Monica", "Good morning!")
######################
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
greet("Bruce", msg = "How do you do?")
greet(msg = "How do you do?",name = "Bruce")
greet(name = "Bruce",msg = "How do you do?")
#########Error############
# SyntaxError: positional argument follows keyword argument
greet(name="Bruce","How do you do?")
#########Error############
# TypeError: greet() takes from 1 to 2 positional arguments but 3 were given
greet("Bruce", "How do you do?", "test :)")
#########Error############
# SyntaxError: non-default argument follows default argument
def greet(msg = "Good morning!", name):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """
    print("Hello", name + ', ' + msg)

# Using the Python args Variable (like tuple)
def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result

print(my_sum(1, 2, 3))

# Using the Python kwargs Variable (like dict)
def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))

# unpacking operator *args
def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result

list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]

print(my_sum(*list1, *list2, *list3))

my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}
my_merged_dict = {**my_first_dict, **my_second_dict}
print(my_merged_dict)

my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
my_merged_list = [*my_first_list, *my_second_list]
print(my_merged_list)

a = [*"RealPython"]
print(a)

*a, = "RealPython"
print(a)

[*a] = "RealPython"
print(a)





