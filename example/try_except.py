#!/usr/bin/env python3
a = 10
b = 12
c = "a"
try:
   #do something
   #a = a / c
   #a = a / 0
   #a = int(c)
   #c[1]
   raise TypeError

except ValueError:
   # handle ValueError exception
   print("raise ValueError")
   a = 13

except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   print("raise TypeError, ZeroDivisionError")
   a = a / 1

except:
   # handle all other exceptions
   print("OK, other error")


print("a:", a)


# define Python user-defined exceptions
class Error(Exception):
   """Base class for other exceptions"""
   pass

class ValueTooSmallError(Error):
   """Raised when the input value is too small"""
   pass

class ValueTooLargeError(Error):
   """Raised when the input value is too large"""
   pass

# our main program
# user guesses a number until he/she gets it right

# you need to guess this number
number = 10

while True:
   try:
       i_num = int(input("Enter a number: "))
       if i_num < number:
           raise ValueTooSmallError
       elif i_num > number:
           raise ValueTooLargeError
       break
   except ValueTooSmallError:
       print("This value is too small, try again!")
       print()
   except ValueTooLargeError:
       print("This value is too large, try again!")
       print()

print("Congratulations! You guessed it correctly.")
