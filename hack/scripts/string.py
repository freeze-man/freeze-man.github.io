#!/usr/bin/env python3

print("Hello")
print('Hello')

# assign string to a variable
a = "Hello"
print(a)


# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# Strings are Arrays
a = "Hello, World!"
print(a[0])
print(a[3])

# Slicing, indexing
b = "Hello, World!"
print(b[2:5])

# Negative Indexing
b = "Hello, World!"
print(b[-5:-2])

# String Length
a = "Hello, World!"
print(len(a))

# removes any whitespace(or chars)
# from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = " Hello, World!"
print(a.strip("! ")) # return 'Hello, World'

txt = "  banana     "
x = txt.rstrip()
print("of all fruits.", x, "is my favorite")

txt = "banana,,,,,ssaaww....."
x = txt.rstrip(",.asw")
print(x)

txt = "     banana  "
x = txt.lstrip()
print("of all fruits.", x, "is my favorite")

txt = ",,,,,ssaaww.....banana"
x = txt.rstrip(",.asw")
print(x)

# Returns the string in lower case
a = "Hello, World!"
print(a.lower())

# Returns the string in upper case
a = "Hello, World!"
print(a.upper())

# Replaces a string with another string
a = "Hello, World!"
print(a.replace("H", "J"))
print(a.replace("Hello", "Hi"))

# splits the string into substrings if it
# finds instances of the separator
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

""" 
setting the maxsplit parameter to 1,
will return a list with 2 elements!
"""
txt = "apple#banana#cherry#orange"
x = txt.split("#", 1)
print(x)

a = "Hello, World!"
print(a.rsplit(", ")) # return ['Hello', 'World!']

txt = "The rain in Spain stays mainly in the plain"
print(txt.rsplit(" in ", 1))

# Check String
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x) 

# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)
c = a + " " + b
print(c)

# String Format
# Error
age = 36
txt = "My name is John, I am " + age # Error
print(txt)
# Currect
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Escape Character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
"""
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value
"""
txt = 'It\'s alright.'
print(txt) 

txt = "This will insert one \\ (backslash)."
print(txt) 

txt = "Hello\nWorld!"
print(txt) 

txt = "Hello\rWorld!"
print(txt) 

txt = "Hello\tWorld!"
print(txt) 

txt = "Hello \bWorld!"
print(txt) 

txt = "\110\145\154\154\157"
print(txt) 

txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

# Returns the number of times a 
# specified value occurs in a string
txt = "This is a test text"
print(txt.count("t"))

# Searches the string for a specified
# value and returns the position of 
# where it was found
txt = "This is a test text"
print(txt.find("tes"))
print(txt.index("x"))
print(txt[10:13])

# check all characters
txt.isalnum()
txt.isalpha()
txt.isdigit()

txt = "Thisisatesttext"
txt.isalpha()

# join with char at elements of an iterable
",".join("test")
",".join(["this is", " a test"])

#check start or end of string
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)
x = txt.endswith("world.")
print(x)
x = txt.endswith("my world.", 18, 27) # 18, 27
print(x)

x = txt.startswith("Hello")
print(x)
x = txt.startswith("wel", 7, 20)
print(x)


# iterable string
a = "Hello World! "
print(a * 2)



