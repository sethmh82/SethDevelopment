# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 11:50:10 2021

@author: SethHarden
"""

import math
# Add any extra import statements you may need here
import heapq
"""


GIVEN: list = [0,1,2,3] list[n]

RETURN: output = [1,2,3] output [o]

output = l1 * l2 * l3


Can the integers in the list be sorted? should we sort them?


"""

# Add any helper functions you may need here


def findMaxProduct(arr):
  pq = []
  length = len(arr)
  
  #return empty if list is empty
  if length == 0:
    return []
  
  #return negative value if length is 1 or 2
  elif length == 1:
    return [-1]
  elif length == 2:
    return [-1, -1]
  
  # setup our answer list with N places
  answer = [0] * length
  # if length=5 [0, 0, 0, 0, 0]
  
  #assign the first 2 place a -1
  answer[0] = answer[1] = -1
  # anser is [-1, -1]
  #iterate through each index of our list
  
  
  for i, j in enumerate(arr):
      
    # put -1 in first 2 index
    if i < 2:
      heapq.heappush(pq, j)
      #or push the largest values to 
    else:
      heapq.heappush(pq, j)
      #get the 3 largest values, returns [n1, n2, n3]
      largest3 = heapq.nlargest(3, pq)
      #get product of 3 largest values
      
      answer[i] = largest3[0] * largest3[1] * largest3[2]
      
  return answer







# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
  print('[', n, ']', sep='', end='')

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  arr_1 = [1, 2, 3, 4, 5]
  expected_1 = [-1, -1, 6, 24, 60]
  output_1 = findMaxProduct(arr_1)
  check(expected_1, output_1)

  arr_2 = [2, 4, 7, 1, 5, 3]
  expected_2 = [-1, -1, 56, 56, 140, 140]
  output_2 = findMaxProduct(arr_2)
  check(expected_2, output_2)


  # Add your own test cases here
  