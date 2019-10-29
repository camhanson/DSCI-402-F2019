#Flatten - takes a list and puts all items into a single list
def flatten(List):
    result = []
    for i in List:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result


#Powerset - the set of all possible subsets for a set
def powerset(List):
    if len(List) == 0:
        return [[]]
    else:
        rest = powerset(List[1:])
        L = []
        for x in rest:
            L.append([List[0]] + x) 
    return L + rest


#Permutation - all possible arrangements of items in a list
def all_perms(List):
    if len(List) == 1:
        return [List]
    result = [] # resulting list
    for i in List:
        rest = [x for x in List if x != i]
        A = all_perms(rest)
        for b in A:
            result.append([i] + b)
    return result
   
   
#Number Spiral         
import numpy as np           
def spiral(n, end_corner):
    starting_corner = {1:[0,0], 2:[0,n-1], 3:[n-1,0], 4:[n-1,n-1]}
    curr_value = (n*n) -1 
    dir = [[1,0], [0,1], [-1,0], [0,-1]]
    curr_pos = starting_corner[end_corner]
    starting_dir = {1:dir[0], 2:dir[1], 3:dir[2], 4: dir[3]}
    curr_dir = starting_dir[end_corner]
    matrix = np.negative(np.ones((n,n),dtype=int))
    
    while curr_value >= 0:
        row = curr_pos[0]
        col = curr_pos[1]
        matrix[row][col] = curr_value
        curr_value -=1
        if matrix[row][col] != -1 and curr_pos + curr_dir not in range(matrix[row][col]):
            curr_dir = starting_dir[end_corner + 1]
            curr_pos += curr_dir
    return matrix

        
    
