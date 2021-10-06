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

#String Formatting

def print_formatted(number):
    # your code goes here
    
    
    l=str(len(bin(number))-2)

    out = ""
    for x in range(1,number+1):
        
        line = "{0:>" + l + "d} {1:>" + l + "o} {2:>" + l + "X} {3:>" + l + "b}"
    
        out = out + line.format(x,x,x,x) + "\n"
    
    print(out)
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

#Alphabet Rangoli

def print_rangoli(size):
    # your code goes here



    alph="abcdefghijklmnopqrstuvwxyz"
          
    out = ""
    line = ""
    M = (size*4) - 3
    for x in range(size-1):
        if(x == 0):
            line = alph[size-1:size].center(M,"-")
        else:
            line = "-".join(alph[size-1:size-1-x:-1])+ "-" + "-".join(alph[size-1-x:size])
            line = line.center(M,"-")    
        out = out + line + "\n"

    cent = "-".join(alph[size-1::-1])+ "-" + "-".join(alph[1:size])
    
    if size > 1 and size < 27:
        print(out + cent + out[::-1])
    elif size == 1:
        print("a")


    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

#Capitalize!

def solve(s):

    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

#The Minion Game

def minion_game(string):
    s = string

    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s)-i)
        else:
            stusc += (len(s)-i)

    if kevsc > stusc:
        print ("Kevin", kevsc)
    elif kevsc < stusc:
        print ("Stuart", stusc)
    else:
        print ("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

#Merge the Tools!

def merge_the_tools(string, k):
    
    for part in zip(*[iter(string)] * k):
        d = dict()
        print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    
#Introduction to Sets

def average(array):
    
    return sum(set(array))/len(set(array))
    
    
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

#No Idea!

lung = input()
arr = input().split()
A = set(input().split())
B = set(input().split())

count = 0
for x in range(len(arr)):
    if arr[x] in A:
        count += 1
    if arr[x] in B:
        count -= 1

print(count)

#Symmetric Difference

lungA = input()
A = set(map(int,input().split()))
lungB = input()
B = set(map(int,input().split()))

out = list(A.symmetric_difference(B))
out.sort()

for x in out:
    print(x)

#Set .add()

A = set()

for _ in range(int(input())):
    A.add(input())

print(len(A))

#Set .discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split()))
N = int(input())

out = ""
end = ")"
for _ in range(N):
    l = input().split()
    if l[0]!= "pop":
        out = "s."+l[0]+"("
        for x in range(1,len(l)):
            out = out+l[x]+","
        if out.endswith(","):
            out = out[:-1]
        out = out + end
        eval(out)
    else:
        s.pop()

print(sum(s))

#Set .union() Operation

input()
A = set(map(int,input().split()))
input()
B = set(map(int,input().split()))

print(len(A.union(B)))

#Set .intersection() Operation

input()
A = set(map(int,input().split()))
input()
B = set(map(int,input().split()))

print(len(A.intersection(B)))

#Set .difference() Operation

input()
A = set(map(int,input().split()))
input()
B = set(map(int,input().split()))

print(len(A.difference(B)))

#Set .symmetric_difference() Operation

input()
A = set(map(int,input().split()))
input()
B = set(map(int,input().split()))

print(len(A.symmetric_difference(B)))

#Set Mutations

n = int(input())
s = set(map(int, input().split()))
N = int(input())

out = ""
end = ")"
for _ in range(N):
    l = input().split()
    l2 = list(map(int,input().split()))
    out = "s."+l[0]+"(" + str(l2) + ")"
    eval(out)

print(sum(s))

#The Captain's Room

k = int(input())
arr = list(map(int, input().split()))
arr.sort()
check = False


for x in range(0,len(arr)-1,k):
    if arr[x] != arr[x+1]:
        print(arr[x])
        check = True
        break

if not check:
    print(max(arr))

#Check Subset

for _ in range(int(input())):
    input()
    A = set(map(int,input().split()))
    input()
    B = set(map(int,input().split()))
    
    print(A.issubset(B))

#Check Strict Superset

A = set(map(int,input().split()))
n = int(input())
i=0
check = True
while i<n and check:
    B = set(map(int,input().split()))
    if not A.issuperset(B):
        check = False
    i += 1
    
print(check)

#collections.Counter()

from collections import Counter

input()
CounterS = Counter(map(int,input().split()))
keys = CounterS.keys()
count = 0
for _ in range(int(input())):
    inp = list(map(int, input().split()))
    if inp[0] in keys:
        count += inp[1]
        CounterS[inp[0]] -= 1
        if CounterS[inp[0]] < 1:
            CounterS.pop(inp[0])

print(count)

#DefaultDict Tutorial

from collections import defaultdict

A = defaultdict(list)
B = list() 

n, m = map(int, input().split())

for y in range(1, n+1):
    x = str(input())
    A[x].append(y)

for z in range(1, m+1):
    x = str(input())
    B.append(x)
    
for i in B:
    if i in A.keys():
        for x in A[i]:
            print(x, end=" ")
    else:
        print(-1, end=" ")
    print("")

#Collections.namedtuple()

N = int(input())
l = list()
tot = 0
title = list(input().split())
marksIndex = title.index("MARKS")

for _ in range(N):
    l = input().split()
    tot += int(l[marksIndex])

print(tot/N)

#Collections.OrderedDict()

from collections import OrderedDict

d = OrderedDict()
l = list()

for _ in range(int(input())):
    l = input().split()
    l[-1] = int(l[-1])
    
    if " ".join(l[:-1]) in d: 
        d[" ".join(l[:-1])] += l[-1]
    else:
        d[" ".join(l[:-1])] = l[-1]

for x in d:
    print(f'{x} {d[x]}')
    
#Word Order

from collections import defaultdict

d = defaultdict(int)

for _ in range(int(input())):
    d[input()] += 1
    
print(len(d))

for x in d:
    print(d[x], end=" ")
    
#Collections.deque()

from collections import deque

n = int(input())
s = deque()

out = ""
end = ")"
for _ in range(n):
    l = input().split()
    if l[0]!= "pop":
        out = "s."+l[0]+"("
        for x in range(1,len(l)):
            out = out+l[x]+","
        if out.endswith(","):
            out = out[:-1]
        out = out + end
        eval(out)
    else:
        s.pop()

for x in s:
    print(x, end=" ")

#Company Logo

from collections import defaultdict, OrderedDict, Counter

d = defaultdict(int)
temp=0
s = sorted(input())

for x in range(len(s)):
    d[s[x]] += 1

d2 = OrderedDict(d)
d3 = Counter(d2).most_common(3)
for x in d3:
    print(f'{x[0]} {x[1]}')

#Piling Up!

for t in range(int(input())):
    input()
    lst = list(map(int, input().split()))
    l = len(lst)
    i = 0
    while i < l - 1 and lst[i] >= lst[i+1]:
        i += 1
    while i < l - 1 and lst[i] <= lst[i+1]:
        i += 1
    if i == l - 1: 
        print("Yes")
    else:
        print("No")








