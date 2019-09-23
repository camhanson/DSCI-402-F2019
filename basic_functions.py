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
        
#Fibonacci Formula
def fib(a,b,n):
    x = 0
    while n == 1:
        x = a
    while n == 2:
        x = b
    while n > 2:
        x = (n-1) + (n-2)
    return x 
   
    
#Recursive fibonacci formula
def rfib(a,b,n):
    if n == 1:
        return a
    if n == 2:
        return b 
    else:
        return rfib(a,b,n-2) + rfib(a,b, n-1)

    
    