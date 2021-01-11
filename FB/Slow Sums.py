# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 13:30:11 2021

@author: SethHarden
"""


"""
Slow Sums
Suppose we have a list of N numbers, and repeat the following operation until we're left with only a single number: Choose any two numbers and replace them with their sum. Moreover, we associate a penalty with each operation equal to the value of the new number, and call the penalty for the entire list as the sum of the penalties of each operation.
For example, given the list [1, 2, 3, 4, 5], we could choose 2 and 3 for the first operation, which would transform the list into [1, 5, 4, 5] and incur a penalty of 5. The goal in this problem is to find the worst possible penalty for a given input.

"""
import bisect 

def maximizeSum(arr, n) :
    
  ans = 0
  arr.sort()
  print(arr)
  while n >= 2:
    v = arr.pop() + arr.pop()
    ans += v
    bisect.insort(arr, v)
    n = len(arr)
  return ans
 
# Driver code 
if __name__ == "__main__" : 
 
    arr = [4, 2, 1, 3] 
    n = 4
    print(maximizeSum(arr, n))
 
