# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 21:22:00 2021

@author: SethHarden

# TWO SUM
'''

Given an array of integers (nums) and an integer (taget).

Visualize the inputs:     nums = [2,7,11,15]    target = 9

Return indices of the two numbers such that they add up to target.

indices = i of nums **because it's the index NOT value we are returning
So, 2 is at [0] and 7 is at [1]
Visualize the output: return [0,1]

Visualize possible algoritms: nums[i] + nums[i(2)] == 9

You may assume that each input would have exactly one solution.
*When we find 2 numbers we can stop searching.

You may not use the same element twice.
*This tells us to use data collection that doesnt allow doubles.
Which are a Dictionary = {} or Set = ()
BUT Sets are immutable so a Dictionary (hash table) it is!

Return the answer in any order.
*We don't need to sort anything, meaning our time/space complexity must be O(n)

CONSTRAINTS
for target=n:       max(nums) > n > min(nums)

     2 <= nums.length <= 10**3
-10**9 <= nums[i]     <= 10**9
-10**9 <= target      <= 10**9


How can we collect this data?
enumerate()
range()
for i in nums:

What can we collect?
1. Compliment or Difference of each number to the target. *Also distance
2. Value of each number
3. Index of each number

Don't collect
1. Sum
2. Product

diff of 9-2 = 7
diff of 9-7 = 2

if target < nums[i]
We don't need to collect these:
diff of 9-11 <= 0
diff of 9-15 <= 0

How can we structure this data?

dict = {       }

'''

# 2 7 11 15
# 0 1 2  3


# dict { 2:0 }


class Solution(object):
    
   
#     def listFilter(numbers, target):
#         short_list = [x for x in numbers if x <= target]
#         return short_list
   
# # BRUTE FORCE      
# # This is O(n^2) / O(1)   
#     def twoSum(numbers, target):
     
#         for i_dex in range(len(numbers)): #O(n)
#             #loop through the indices
            
#             for j_dex in range(len(numbers)): #O(n)
#                 #nested loop through indices
                
#                 if i_dex != j_dex and numbers[i_dex] + numbers[j_dex] == target: 
#                     # if the indices are different 
#                     # but the sum values = target 

#                     return [i_dex, j_dex] 
#                 # we know that there is one guaranteed answer 
#                 # so when it does we just return the answer
#         return "No two sum solution found"


# Two-Pass Hash Table
# This is O(n) 

    def twoSum(numbers, target):
        
        dictionary = {}
        
        for index, value in enumerate(numbers):
            dictionary[value] = index

        
        for index, value in enumerate(numbers):
            complement = target - numbers[index] 
            
            if complement in dictionary:
                return [index, dictionary[complement]]
            
        return "No two sum solution found"
                
"""   
# One-pass Hash Table
# This is O(n) / O(1)
    def twoSum(numbers, target):
        
        dictionary = {}
        
        for index, value in enumerate(numbers):
            
            complement = target - value

            if complement not in dictionary:

                dictionary[value] = index

            else:

                return [dictionary[complement], index]
            
        return "No two sum solution found"
"""                  

numbers = [1,2,6,7,11,15]
target = 9
print(Solution.twoSum(numbers, target))



                


