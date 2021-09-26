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

#Finding the percentage

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    
    out = 0
    for x in range(3):
        out = out + student_marks[query_name][x]
    out = out/3
    print("%.2f" %out)

#Lists

if __name__ == '__main__':
    N = int(raw_input())
    
    lista = []
    out = ""
    end = ")"
    for _ in range(N):
        inp = raw_input()
        l = inp.split(" ")
        if l[0] != "print":
            out = "lista."+l[0]+"("
            for x in range(1,len(l)):
                out = out+l[x]+","
            if out.endswith(","):
                out = out[:-1]
            out = out + end
            eval(out)
        else:
            print(lista)

#Tuples

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t = tuple(integer_list)
    print(hash(t))

#sWAP cASE

def swap_case(s):
    s = s.swapcase()
    return s

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result

#String Split and Join

def split_and_join(line):
    return line.replace(" ","-")

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result


























