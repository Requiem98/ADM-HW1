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

#What's Your Name?

def print_full_name(first, last):
    # Write your code here
    out = "Hello {0} {1}! You just delved into python."
    print(out.format(first,last))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
    
#Mutations

def mutate_string(string, position, character):
    string = string[0:position] + character + string[position+1:]
    
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    
#Find a string

def count_substring(string, sub_string):
    count = 0
    for x in range(len(string)):
        temp = ""
        if x <= len(string)-len(sub_string):
            for y in range(len(sub_string)):
                temp = temp + string[x+y]
        if temp == sub_string:
            count = count + 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    
#String Validators

if __name__ == '__main__':
    s = input()
    
    out = "False False False False False"
    out = out.split()
    
    for x in s:
        if x.isalnum() and out[0] != "True":
            out[0] = "True"
        if x.isalpha() and out[1] != "True":
            out[1] = "True"
        if x.isdigit() and out[2] != "True":
            out[2] = "True"
        if x.islower() and out[3] != "True":
            out[3] = "True"
        if x.isupper() and out[4] != "True":
            out[4] = "True"

    for y in out:
        print(y)

#Text Alignment

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#Text Wrap

import textwrap

def wrap(string, max_width):
    out = ""
    count = 1
    
    for x in range(len(string)):
        if count%max_width==0:
            out = out + string[count-max_width:count] + "\n"
            if((len(string)-x-1) < max_width):
                out = out + string[x+1:]
        count = count+1
    return out

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

#Designer Door Mat

N,M = map(int,input().split())



gra = ".|."
w = "WELCOME".center(M,"-")
out = ""
line = ""
for x in range((N)//2):
    if(x == 0):
        line = gra.center(M,"-")
    else:
        gra = gra + ".|."*2
        line = gra
        line = line.center(M,"-")    
    out = out + line + "\n"

print(out + w + out[::-1])























