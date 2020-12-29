# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 12:20:40 2020

@author: SethHarden
"""

import math
# Add any extra import statements you may need here

"""
We receive 2 arrays (A,B)
We are told their lengths with N.

Determine if there is a way to make A == B by reversing any sub arrays from array B (any number of times)

what do we need to know about the arrays.
what can we do with the arrays?
how can we compare it?

Return a boolean value (true, false) 

Let's setup our array scanning system.

QUESTIONS?
The arrays have length N, N should always be equal
If they are not the same length can we automatically return a false?


----------
We can go through each index of A and see if that exists in any of B's indexes.
This is like
O(N**2)


Potential libraries 
from bisect import bisect_left

"""

# Add any helper functions you may need here


def are_they_equal(array_a, array_b):
    outcome = "False"
  
    for i in array_a:  #O(n)
        if i in array_b: #O(n**2)
            outcome = "True"
        else:
            outcome = "False"
    return outcome
      
      










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
  n_1 = 4
  a_1 = [1, 2, 3, 4]
  b_1 = [1, 4, 3, 2]
  expected_1 = True
  output_1 = are_they_equal(a_1, b_1)
  check(expected_1, output_1)

  n_2 = 4
  a_2 = [1, 2, 3, 4]
  b_2 = [1, 2, 3, 5]  
  expected_2 = False
  output_2 = are_they_equal(a_2, b_2)
  check(expected_2, output_2)

  # Add your own test cases here
  