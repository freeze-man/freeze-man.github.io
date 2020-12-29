#!/usr/bin/env python3
counter = 0
"""
counter = 0

while counter < 10:
    print("Inside loop")
    counter = counter + 1
    print("before break !!!")
    if counter == 5:
        break
    #break
    print("after if check condition [for break] !!!")
else:
    print("Inside else")
"""
while True:
	print("Inside loop")
	counter = counter + 1
	print("before break !!!")
	if counter == 5:
		print("counter == 5")
		break
	else:
		print("counter is :", counter)

