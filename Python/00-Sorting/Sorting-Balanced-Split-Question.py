# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 18:57:54 2020

@author: SethHarden
"""
import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


# Split an array into two subsequences (a, b)
# to see if the sum of of the integers in both are ==

def findSplitPoint(arr, n):
  
  leftSum = 0
  #traverse
  for i in range(0, n):
    #add them
    leftSum += arr[i]
    rightSum = 0
    
    for j in range(i+1, n):
      rightSum += arr[j]
    
    if (leftSum == rightSum):
      return i+1
    
  return -1

def balancedSplitExists(arr):
  # Write your code here
  n = len(arr) 
  splitArray = findSplitPoint(arr, n)
  
  if (splitArray == -1 or splitArray == n ):
    return False
  
  for i in range(0, n):
    if(splitArray == i):
      print("True")
    return True




# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

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
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  arr_1 = [2, 1, 2, 5]
  expected_1 = True
  output_1 = balancedSplitExists(arr_1)
  check(expected_1, output_1)

  arr_2 = [3, 6, 3, 4, 4]
  expected_2 = False
  output_2 = balancedSplitExists(arr_2)
  check(expected_2, output_2)

  # Add your own test cases here 