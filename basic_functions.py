#Basic Functions
import random as rnd

# Add two numbers
def add_2(x,y):
    return x + y
 
#Returns unique number pairs over 1...n. 
def unique_pairs(n):
    nums = list(range(1, n + 1))
    return[(x,y) for x in nums for y in nums if x < y]
    
#A 'procedure' - aka a function which does not return anything    
def say_hi(person):
    print('Hi ' + str(person) + '!!')

#Return a random floating point number in the range (a,b)
def randfloat(a,b):
    return a + (rnd.random() * b - a)

#Variable-Length input function example 1:
def var_length_f(a,b,*c):
    print(a)
    print(b)
    print(c)

#fzip implementation
def fzip(f,*lists):
    return [f(*list(x)) for x in zip(*lists)]
    
#Calculate the sum from a to b inclusive.
def sum_range(a,b):
    curr_total = 0
    i = a 
    while i <= b:
        curr_total += i
        i+=1
    return curr_total
    
#Recursive definition of sum_range
def srr(a,b):
    if a == b:
        return a
    else: #technically don't need else
        return srr(a, b-1) + b
        
        
#Recursive Fibonacci Number Generator
#Returns the nth element in the sequence give a and be as first two elements.
def rfib(a,b,n,h={}):
    if n == 1:
        return a
    if n == 2:
        return b 
    if n in h:
        return h[n]
    else:
        h[n] = rfib(a,b,n-2) + rfib(a,b, n-1)
        return h[n]

# Recursive reversal of a list
def rev(l):
    if len(l) == 0: 
        return []
    return [l[-1]] + rev(l[:-1])
    
#Cartesian product
def icp(A,B):
    p = []
    for i in A:
        for j in B:
            p.append((i,j))
    return p
      
#Recursive Cartesian Product
def cp(a,*b) : 
    if not b:
        return [[x] for x in a]
    else:
        return [[x,] + y for x in a for y in cp(b[0],*b[1:])]

#Recursive Factorial Function    
#by definition 0! is 1
def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)

#Recursive Combinations
def combs(s,k) :
    if len(s) == k:
        return [s]
    else:
        return [[s[0]] + combs(s[1:],k) + combs(s[1:],k)]