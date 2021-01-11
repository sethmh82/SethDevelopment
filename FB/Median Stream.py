# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 10:54:34 2021

@author: SethHarden
"""
import math
import collections


def findPositions(arr, x):
    arrPos = collections.deque()
    for i, num in enumerate(arr):
        arrPos.append([num, i+1])
        
    ans=[]
    
    def iterate(arrPos, n):
        q = collections.deque()
        mx = -1
        mxp = -1
        
        while n > 0 and arrPos:
            a, pos = arrPos.popleft()
            if a > mx:
                mx = a
                mxp = pos
                
            q.append([a, pos])
            n -= 1
            
        ans.append(mxp)
                
        firsttime = True
        while q:
            a, pos = q.popleft()
            if a != mx:
                arrPos.append([a - 1 if a - 1 >= 0 else 0, pos])
            elif a == mx:
                if firsttime:
                    firsttime = False
                else:
                    arrPos.append([a - 1 if a - 1 >= 0 else 0, pos])
                    
    n = x
    
    while x > 0 and arrPos:
        iterate(arrPos, n)
        x -= 1
    return ans



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
  n_1 = 6
  x_1 = 5
  arr_1 = [1, 2, 2, 3, 4, 5]
  expected_1 = [5, 6, 4, 1, 2]
  output_1 = findPositions(arr_1, x_1)
  check(expected_1, output_1)

  n_2 = 13
  x_2 = 4
  arr_2 = [2, 4, 2, 4, 3, 1, 2, 2, 3, 4, 3, 4, 4]
  expected_2 = [2, 5, 10, 13]
  output_2 = findPositions(arr_2, x_2)
  check(expected_2, output_2)

  # Add your own test cases here
  

