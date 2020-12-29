# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 14:26:41 2020

@author: SethHarden
"""
import math
# Add any extra import statements you may need here
"""

We have a list
Repeat operation until only 1 number remains
Pick any 2 numbers and replace them with their sum (a+b)=c
We create a penalty object is = c
Total penalty = sum of all operations

What are we trying to do?
Take in a list of numbers.
Add 2 numbers from the list together.
Continue this until there is only 1 number.

[1, 2, 3] = [3, 3] = [6]
"""

# Add any helper functions you may need here

  
def getTotalTime(arr):
    collection = 0
    while i in enumerate(arr.sorted()):
      collection += arr[i] + arr[i+1]
    n = sum(collection)
    return n








# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

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
  arr_1 = [4, 2, 1, 3]
  expected_1 = 26
  output_1 = getTotalTime(arr_1)
  check(expected_1, output_1)

  arr_2 = [2, 3, 9, 8, 4]
  expected_2 = 88
  output_2 = getTotalTime(arr_2)
  check(expected_2, output_2)

  # Add your own test cases here
  