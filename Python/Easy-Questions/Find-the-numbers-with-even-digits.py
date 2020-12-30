# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 11:32:23 2020

@author: SethHarden
"""

#class Solution:
nums = [12,345,2,6,7896,22]
def findNumbers(self, nums):
        
    output = 0 #set our counter to even 0

    for i in nums: #loop through the array
           i = str(i) #we need to convert it to a string so we can easily append
           if len(i) % 2 == 0: #check to see if we're even or odd
               output += 1 #add to count
    
    return output
x = ""
x = findNumbers(x, nums) 
print(x)  
    
    # numbers = sum(nums.isdigit() for nums in s)