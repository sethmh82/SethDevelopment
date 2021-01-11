# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 11:34:57 2021

@author: SethHarden
"""

import math

import heapq

def maxCandies(arr, k):

  bags = []
  minutes = k
  
  #push the list into a heap
  for i in arr:
    heapq.heappush(bags, -i)
  
  #set our minimum
  answer = 0
  
  #while we have time and there are bags
  while minutes > 0 and bags:
    #get the absolute value of everything in our bag
    max_candy = abs(heapq.heappop(bags))
    answer += max_candy
    heapq.heappush(bags, - (max_candy // 2))
    minutes -= 1
    
  return answer
	





def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  n_1, k_1 = 5, 3
  arr_1 = [2, 1, 7, 4, 2]
  expected_1 = 14
  output_1 = maxCandies(arr_1, k_1)
  check(expected_1, output_1)

  n_2, k_2 = 9, 3
  arr_2 = [19, 78, 76, 72, 48, 8, 24, 74, 29]
  expected_2 = 228
  output_2 = maxCandies(arr_2, k_2)
  check(expected_2, output_2)

  # Add your own test cases here
  