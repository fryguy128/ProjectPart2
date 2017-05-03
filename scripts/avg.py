#! /usr/bin/python

import fileinput

x = 0
sum = 0
for i in fileinput.input():
    sum += float(i.strip())
    x+= 1
print(sum/x)
