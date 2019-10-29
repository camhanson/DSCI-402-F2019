#One way to import/ use modules
import basic_functions as bf
print(bf.add_2(4,5))

#Another way to import/use modules
#import basic_functions
#print(basic_functions.add_2(10,12))

#Another way
#from basic_functions import *
#print(add_2(31,33))

#Another way
#from basic_functions import add_2
#print(add_2(29,44))

#Test unique pairs
print(' ')
print('-----Testing unique pairs-----')
print(bf.unique_pairs(10))


#Test say_hi.
print(' ')
print('-----Testng say_hi-----')
print(bf.say_hi('Luke'))
print(bf.say_hi('Carly'))
print(bf.say_hi([1,2,3]))

#Testing randomfloat function
print(' ')
print('-----Testing Random Float-----')
for i in range(10):
    print(str(bf.randfloat(1,25))) 
    
#Testing variable length input function example 1:
print(' ')
print('----- Testing var_length_f-----')
bf.var_length_f('A','B')
bf.var_length_f('x','y','z',1,2,3)


#Test fzip
print(' ')
print('-----Testing fzip-----')
f1 = lambda x,y : x + y
f2 = lambda x,y,z : (2 * x) + (y * z)
print(bf.fzip(f1, [1,2,3],[4,5,6]))
print (bf.fzip(f2,[1,2,3,4,5,6],[2,3,4,5,6,7],[3,4,5,6,7,8,]))

#Test Sum Range
print(' ')
print('-------Testing Sum Range-------')
print(bf.sum_range(1,100))
print(bf.sum_range(20,50))

#Test Srr
print(' ')
print('-------Testing Srr-----')
print(bf.srr(1,100))
print(bf.srr(20,50))


#Test Fibonacci Formula
print(' ')
print('-----Testing fib-----')
#print(bf.fib(1,1,5))
#print(bf.fib(2,4,8))


#Test Recursive Fibonacci Formula
print(' ')
print('-----Testing rfib-----')
print(bf.rfib(1,1,8))
print(bf.rfib(2,4,8))
#print(bf.rfib(1,1,150))

#Test rev
print(' ')
print('-----Testing Rev-----')
print(bf.rev(['a','b','c','d','e']))
print(bf.rev(list(range(1,51))))

#test interative cartesian product
print(' ')
print('-----Testing cp-----')
print(bf.icp('a','b'))
print(bf.icp([1,2],[3,4]))

#Test cp
print(' ')
print('-----Testing cp-----')
print(bf.cp(['a','b']))
print(bf.cp([1,2],[3,4],[5,6]))
print(bf.cp([1,2],['a','b'], ['cat','dog'],['yes','no']))

#Test fact
print(' ')
print('-----Testing fact-----')
print(bf.fac(9))
print(bf.fac(20))

#Test Combs
print(' ')
print('-----Testing combs-----')
list = [1,2,3]
print(bf.combs(list,2))
#print(bf.combs(('a,b,c,d,e'),5))
#print(bf.combs('xyz',2))