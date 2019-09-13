#Basic Functions

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
    
    