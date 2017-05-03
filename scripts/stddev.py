#! /usr/bin/python

import fileinput
import math

x = 0
sum = 0
numbers = []
for i in fileinput.input():
    numbers.append(float(i.strip()))
    sum += numbers[x]
    x+= 1
avg = sum/x
for i in numbers:
    sum = (i-avg)*(i-avg)
print math.sqrt(sum)
