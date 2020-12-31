# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 16:38:26 2020

@author: SethHarden

ReOrdering A List of Numbers
"""
class Solution(object):
    
    def reverseString(arr):

        for i in range(len(arr)): # assign i every value in the array

            j = arr.index(min(arr[i:])) # j will store the current position of the value we are going to swith
    
            if (j != i): #if the current position and current value do no match then
        
                #this is the fascinating part of this algorithm:
                    arr = arr[:i] + [ v for v in reversed( arr[i:j+1] ) ] + arr[ j+1: ]
        
                #a nice way to visually see what is happening:
        print(arr)
        return arr
        
    
    reverseString([1,4,3])
    reverseString([3,2,1])
