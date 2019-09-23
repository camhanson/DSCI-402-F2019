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
print('-----Testing unique pairs-----')
print(bf.unique_pairs(10))


#Test say_hi.
print('-----Testng say_hi-----')
print(bf.say_hi('Luke'))
print(bf.say_hi('Carly'))
print(bf.say_hi([1,2,3]))

#bf.say_hi('Luke')
#bf.say_hi('Carly')
#bf.say_hi([1,2,3])

#Testing randomfloat function
print('-----Testing Random Float-----')
for i in range(10):
    print(str(bf.randfloat(1,25))) 
    
#Testing variable length input function example1:
print('----- Testing var_length_f-----')
bf.var_length_f('A','B')
bf.var_length_f('x','y','z',1,2,3)


#Test fzip
print('-----Testing fzip-----')
f1 = lambda x,y : x + y
f2 = lambda x,y,z : (2 * x) + (y * z)
print(bf.fzip(f1, [1,2,3],[4,5,6]))
print (bf.fzip(f2,[1,2,3,4,5,6],[2,3,4,5,6,7],[3,4,5,6,7,8,]))

#Test Sum Range
print('-------Testing Sum Range-------')
print(bf.sum_range(1,100))
print(bf.sum_range(20,50))

#Test Srr
print('-------Testing Srr-----')
print(bf.srr(1,100))
print(bf.srr(20,50))

#Test Fibonacci Formula
print('-----Recursive Fibonacci Formula-----')
print(bf.rfib(2,3,19))
print(bf.rfib(4,7,10))
