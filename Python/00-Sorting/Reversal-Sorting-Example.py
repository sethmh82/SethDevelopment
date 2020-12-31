# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 14:28:50 2020

@author: SethHarden

Minimizing Permutations

"""

import math
# Add any extra import statements you may need here
from collections import defaultdict
# given int(n)
# permuation int(p) from 1 to n (a_1, a_2, ...)

#GOAL
# rearange the elements of the permutation into increasing order.
# repeat the following operation

# select a sub-portion of the permutation,
# a_i, ..., a_i) and reverse its order

# return it in ascending order
# a SimpleReversalSort does not guarantee the smallest number of steps

def minOperations(arr):

    n = 0
    
    for i in range(len(arr)): # assign i every value in the array
  
    # i is the value, j is the list position
    #using .index() we can return the position of a value
      
    #Essentially, we are assigning the value and position to seperate objects (i, j).
        j = arr.index(min(arr[i:])) # j will store the current position of the value we are going to swith
    
        if (j != i): #if the current position and current value do no match then
        
        #this is the fascinating part of this algorithm:
            arr = arr[:i] + [ v for v in reversed( arr[i:j+1] ) ] + arr[ j+1: ]
        
        #a nice way to visually see what is happening:
            print ("Examine: (%d,%d) = %s" % (i, j, arr)) 
            n += 1
      
    print (n)
    return n

minOperations([2,3,9,8,7,6,1])






