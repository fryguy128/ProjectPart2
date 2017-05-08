#! /usr/bin/python
import fileinput

print "\\begin{tabular}{c c c c c c}"
for i in fileinput.input():
    y = 0
    x = 0
    while x < len(i):
        inputString = ""
        while i[x] != ' ' and i[x] != '\n':
            inputString += i[x]
            x += 1
        if i[x] == '\n':
            print inputString,"\\\\"
        else:
            print inputString,"&",
        y=x
        x+=1
print "\\end{tabular}"
