#!/usr/bin/env python3
# Use of break statement inside the loop

for val in "string":
    if val == "i":
        break
    print(val)

print("The end")

for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)

print("The end")

numbers = (1, 2, 3)
num_sum = 0
count = 0
for x in numbers:
        num_sum = num_sum + x
        count = count + 1
        print(count)
        if count == 2:
                break

print("The end")


for x in range(4):
   if (x==2):
      continue
   print(x)
