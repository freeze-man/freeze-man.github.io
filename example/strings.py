s = "hello world!!!"

a = "Hello"
a * 2 #=> "Hello" + "Hello" (2*3 => 2+2+2)
#"HelloHello"

s1 = "Freeze"
s2 = "Man"
s3 = s1 + " " + s2
print(s3) => # "Freeze Man"

word = 'Help' + '=F1'
word = '<' + word*5 + '>'

print("adad" + 64) # error

s[3] #indexing
s[1:3] #slicing
s[:4]
s[5:]
s[0:2]
s[:2] + s[2:]
s[:3] + s[3:]
s[1:100]
s[10:]
s[2:1]
s[-1]
s[-2]
s[-2:]
s[:-2]
s[-0]
s[-100:]
s[-10] # out of range
s[:]
s[::]
s[::1]
s[::2]
s[::-1]
s[::-2]

a, b = "AB"
a, b = "AABB" # ValueError: too many values to unpack (expected 2)
a, b = "AABB"[::2]

s = "HelpA"

# +---+---+---+---+---+
# | H | e | l | p | A |
# +---+---+---+---+---+
# 0   1   2   3   4
#    -5  -4  -3  -2  -1


len(s)

a = "        Hello, World !!!      "
print(a)
a.strip()
a.rstrip()
a.lstrip()
a.rstrip().lstrip()

b = "  ,.,.,.,.,.,.,.,saw....,.,.,.,., Hello, Worls!!!., aaaaaa  ,.,w ssssswsdsad  "
b.strip(" ,wa.s")
b.rstrip(" ,wa.s")
b.lstrip(" ,wa.s")

b.lower()
b.upper()

b = "        Hello, World !!!      "

b.replace(" ", "")
b.replace("!!!", " !")

b = "Hello, World !!!!!!"
b.replace("!!!", " !")

b.replace("Hello", "Hi")

b = "Hello, Hello World!!!"
b.replace("Hello", "Hi")

b.split(",")
b = "Hello, Hello, World!!!"
b.split(",")

txt = "the rain in spain stays mainly in the plain"
txt.rsplit(" in ")
txt.rsplit("in", 2)

"the" in txt
"freeze" not in txt

s = "\"Yes,\" he said."
print(s)

txt.count("n")
txt.count("am")

txt.find("is") #return index
txt.index("is")
txt.index("is", 9)
txt.index("s")
txt.index("s",13)
txt.index("s",12,19)
txt.index("s",13,19)
txt.index("s",13,18)

# with slicing
str = "PQRST"
str[::-1]

allstr = "abcd"
allnum = "12345"

allstr.isalpha()
allnum.isalpha()

#allnum.isallnum()
allnum.isdigit()

allnum = "12345E13"
#allnum.isallnum()
allnum.isdigit() #=> False

",".join("test")

",".join(["Hello", " World!!!"])

p = ["Python", "is", "a", "popular", "language"] 
" ".join(p)

txt = "Hello, welcome to my world."
txt.endswith(".")
txt.endswith("d.")

txt.startswith(".")
txt.startswith("d.")


#Flip String Or List. splited
str_1 = 'python'
for i, value in enumerate(str_1):
     print(i, ':', value)

# 0 : p
# 1 : y
# 2 : t
# 3 : h
# 4 : o
# 5 : n

#String Formatting in Python
#########Option #1: %-formatting#########
name = "Eric"
name = "Hello, %s." % name
print(name)

name = "Eric"
age = 74
st = "Hello, %s. You are %s." % (name, age)
st = "int is, %s. float is %s." % (12.23, 12)
st = "int is, %i. float is %f." % (12.23, 12)
st = "int is, %12i. float is %12.3f. and float is %12.1f." % (12.23, 12, 12.3125)

#########Option #2: str.format()#########
name = "Eric"
age = 74
st = "Hello, {}. You are {}.".format(name, age)
st = "Hello, {1}. You are {0}.".format(age, name)
person = {'name': 'Eric', 'age': 74}
st = "Hello, {name}. You are {age}.".format(name=person['name'], age=person['age'])
st = "Hello, {name}. You are {age}.".format(**person)

age = 64
txt = "My name is John, and I am {}"
txt.format(age)
txt.format(64)
txt = "My name is John, and I am {0}"
txt = "My name is {1}, and I am {0}"
txt.format(age, name)
txt = "My name is John, and I am {age}"
txt.format(age=64)

#########f-Strings: A New and Improved Way to Format Strings in Python#########
name = "Eric"
age = 74
st = f"Hello, {name}. You are {age}."  #'Hello, Eric. You are 74.'
st = f"{2 * 37}" #'74'
st = f"{2 * age}"

def to_lowercase(input):
    return input.lower()

name = "Eric Idle"
st = f"{to_lowercase(name)} is funny." #'eric idle is funny.'
st = f"{name.lower()} is funny." #'eric idle is funny.'

st = f"The \"comedian\" is {name}, aged {age}." #The "comedian" is Eric Idle, aged 74.

#SyntaxError
comedian = {'name': 'Eric Idle', 'age': 74}
st = f"The comedian is {comedian['name']}, aged {comedian['age']}."
#st = f'The comedian is {comedian['name']}, aged {comedian['age']}.'
#st = f"{\"Eric Idle\"}"
#st = f"Eric is {2 * 37 #Oh my!}."

import timeit
timeit.timeit("""name = "Eric"
    age = 74
    '%s is %s.' % (name, age)""", number = 10000)
#0.003324444866599663

timeit.timeit("""name = "Eric"
    age = 74
    '{} is {}.'.format(name, age)""", number = 10000)
#0.004242089427570761

timeit.timeit("""name = "Eric"
    age = 74
    f'{name} is {age}.'""", number = 10000)
#0.0024820892040722242




