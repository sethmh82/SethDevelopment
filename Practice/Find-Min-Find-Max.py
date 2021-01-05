# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 17:40:48 2021

@author: SethHarden
"""
# Python implementation
# to find the minimum
# and maximum amount
 
# Function to find
# the minimum amount
# to buy all candies
 
 
def findMinimum(arr, n, k):
 
    res = 0
    i = 0
    while(n):
 
        # Buy current candy
        res += arr[i]
 
        # And take k
        # candies for free
        # from the last
        n = n-k
        i += 1
    return res
 
# Function to find
# the maximum amount
# to buy all candies
 
 
def findMaximum(arr, n, k):
 
    res = 0
    index = 0
    i = n-1
    while(i >= index):
 
        # Buy candy with
        # maximum amount
        res += arr[i]
 
        # And get k candies
        # for free from
        # the starting
        index += k
        i -= 1
 
    return res
 
# Driver code
arr = [2, 1, 7, 4, 2]
n = len(arr)
k = 2
 
arr.sort()
 
# Function call
print(findMinimum(arr, n, k), " ",
      findMaximum(arr, n, k))
 
# This code is contributed
# by Anant Agarwal.