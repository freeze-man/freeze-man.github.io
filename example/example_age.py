#!/usr/bin/env python3
byy =int(input("Enter birth date(year):"))
bmm =int(input("Enter birth date(month):"))
bdd =int(input("Enter birth date(day):"))
cyy =int(input("Enter current date(year):"))
cmm =int(input("Enter current date(month):"))
cdd =int(input("Enter current date(day):"))
#days = 0
#if bmm < 7 and cmm > 6:
#	days =  cmm - bmm
#	print("add days:", days)
if cdd < bdd:
	cmm -= 1
	cdd += 30
day = cdd - bdd

if cmm < bmm:
	cyy -= 1
	cmm += 12
month = cmm - bmm
year = cyy - byy

#days += year % 4
#print("add days:", days)

days = days + day + month * 30 + year * 365
hh = days * 24
mm = hh * 60
ss = mm * 60
print("Old is : {0} -> years | {1} -> months | {2} -> days".format(year, month, day))
print("{0} -> total days".format(days))
print("{0} -> Hours | {1} -> Minutes | {2} -> Seconds".format(hh, mm, ss))
