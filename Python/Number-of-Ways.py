# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 12:51:26 2020

@author: SethHarden
"""
"""
def findPairs(lst, K):  
    res = [] 
    while lst: 
        num = lst.pop() 
        diff = K - num 
        if diff in lst: 
            res.append((diff, num)) 
          
    res.reverse() 
    return res 
      
# Driver code 
lst = [1, 5, 3, 7, 9] 
K = 12
print(findPairs(lst, K)) 

"""


def numberOfWays(arr, k):
  col = [] #we setup a collector for our differences
  while arr: #we go in order through the array that was passed to our class i.e. [ 1, 5 ,3 ,3 ,3 ] and let's say K = 6
    # num = arr.pop() #we assign (in Order) the object "num" to the number coming out of the array.
    diff = int(k) - int(arr.pop()) # it assigns the operation of K-n to the object "diff"
    if diff in arr: #then we say if running the operation contained in the object "diff" 
      col.append((diff, arr.pop())) #then add that number to our collector
      
      #so if we were to print this out now it would look like
      # [(1,5), (5,1), (3,3) ]
      
  col.reverse()   
 # n = len(col)
 
  return col

k_3 = 6
arr_3 = [1, 5, 3, 3, 3] 
print(numberOfWays(arr_3, k_3))




from unittest import TestCase


def numberOfWays(arr, k):
    if not arr:
        return 0
    maps = {}
    counter = 0
    for num in arr:
        diff = k - num
        if num in maps:
            counter += maps[num]
            maps[num] += 1
        else:
            maps[diff] = 1
    return counter


class TestPairSums(TestCase):
    def setUp(self) -> None:
        self.arr_1 = [1, 2, 3, 4, 3]
        self.arr_2 = [1, 5, 3, 3, 3]
        self.k = 6

    def test_pair_sums(self) -> None:
        self.assertEqual(2, numberOfWays(self.arr_1, self.k))
        self.assertEqual(4, numberOfWays(self.arr_2, self.k))