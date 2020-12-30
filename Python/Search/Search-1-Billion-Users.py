# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 15:50:49 2020

@author: SethHarden
"""

import math
# Add any extra import statements you may need here
"""
We have N different apps with differnt user growth rates.

At a given time (t)

Measure in days (d)

the number of users using an app is g ^ t
can be a float

G = growth rate

Apps launch at same time user can only use 1 app at a time
We want to know
How many total users there are when you add together the number of users from each
After how many full days will we have 1 billion total users across the N apps?


We are sliding
1.0 < GR < 2.0
1 <= N <= 1,000
"""

# Add any helper functions you may need here
# lets create a function for the passing of time
billion = 1000000000

# set the lower boundry
def getDays(arr, t): #O(log n)
  days_passed = 0
  for g in arr:
    days_passed += (g ** t)
  return days_passed
# find the upper boundry
def boundry(arr, low, high): #O(log n)
  while low < high:
    mid = low + (high - low) // 2
    if getDays(arr, mid) < billion:
      low = mid + 1
    else:
      high = mid
  return high


def getBillionUsersDay(growthRates):
  i = 1
  app_users = getDays(growthRates, i) #we inherit the results
  if app_users >= billion:
    return 1 #return 1 day if we're already over.
  
  while app_users < billion:
    i *= 2
    app_users = getDays(growthRates, i)
    
  print(growthRates)
  print(boundry(growthRates, i // 2, i))
  return boundry(growthRates, i // 2, i)



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
  test_1 = [1.1, 1.2, 1.3]
  expected_1 = 79
  output_1 = getBillionUsersDay(test_1)
  check(expected_1, output_1)

  test_2 = [1.01, 1.02]
  expected_2 = 1047
  output_2 = getBillionUsersDay(test_2)
  check(expected_2, output_2)

  # Add your own test cases here