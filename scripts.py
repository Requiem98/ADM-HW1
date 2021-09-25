#!/bin/python

import math
import os
import random
import re
import sys



#Say "Hello, World!" With Python

if __name__ == '__main__':
    print "Hello, World!"
   
#Python If-Else

if __name__ == '__main__':
    n = int(raw_input().strip())

    if n%2 != 0:
        print("Weird")
    
    elif n >=2 and n <=5:
        print("Not Weird")
    
    elif n >= 6 and n <= 20:
        print("Weird")
    
    elif n > 20:
        print("Not Weird")

#Arithmetic Operators

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    
    print(a+b)
   
    print(a-b)

    print(a*b)

#Python: Division

from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

    print(a//b)
    print(a/b)

#Loops

if __name__ == '__main__':
    n = int(raw_input())
    
    for x in range(n):
        print(x**2)

#Write a function

def is_leap(year):
    leap = False
    
    if year%4 == 0:
        leap = True
        if year%100 == 0:
            leap = False
            if year%400 == 0:
                leap = True
    
    return leap

#Print Function

from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    out = ''
    for x in range(1,n+1):
        out = out + str(x)
    print(out)

#List Comprehensions

if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    
    out = []
    for a in range(x+1):
        for b in range(y+1):
            for c in range(z+1):
                if a+b+c != n:
                    out.append([a,b,c])
    print(out)

#Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    
    maxx = arr[0]
    out = arr[0]
    
    for x in arr:
        if x > maxx:
            out = maxx
            maxx = x
        if x < maxx and x > out:
            out = x
        if maxx == out:
            out = x
    print(out)

#Nested Lists

if __name__ == '__main__':
    clas = []
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        clas.append([name,score])
    
    minn = clas[0][1]
    outG = clas[0][1]

    for x in range(len(clas)):
        if clas[x][1] < minn:
            outG = minn
            minn = clas[x][1]
        if clas[x][1] > minn and clas[x][1] < outG:
            outG = clas[x][1]
        if minn == outG:
            outG = clas[x][1]
            
    clas.sort()
    
    for x in range(len(clas)):
        if clas[x][1] == outG:
            print(clas[x][0])
    
    

#

#

#

#





























