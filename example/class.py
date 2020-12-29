#!/usr/bin/env python3

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

  def printyear(self):
    print(self.graduationyear)

class Student(Person):
  def __init__(self, fname, lname, year):
    # super().__init__(fname, lname)
    Person.__init__(self, fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

#x = Student("Mike", "Olsen", 2020)
#x.welcome()
#print("grade of year:", x.graduationyear)
#print("firstname:", x.firstname)
#print("lastname:", x.lastname)
#x.printname()
#x.printyear()

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x,self.y)

    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        # return print("(x,y):", x, y)
        return Point(x,y)


p1 = Point(2,3)
p2 = Point(-1,2)
print(p1)
print(p2)

print(p1 + p2)
