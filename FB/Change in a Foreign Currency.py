# -*- coding: utf-8 -*-
"""
Change in a Foreign Currency
You likely know that different currencies have coins and bills of different denominations. In some currencies, it's actually impossible to receive change for a given amount of money. For example, Canada has given up the 1-cent penny. If you're owed 94 cents in Canada, a shopkeeper will graciously supply you with 95 cents instead since there exists a 5-cent coin.


Created on Mon Jan 11 18:00:05 2021

@author: SethHarden
"""

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def canGetExactChange(targetMoney, denominations):

    dp = [0] * (targetMoney + 1)
    dp[0] = 1
    
    for i in denominations:
      for x in range(i, targetMoney + 1):
          
        dp[x] += dp[x - i]
    found = int(dp[targetMoney])   
    if found >= 1: return True
    else: return False
	











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
  target_1 = 94
  arr_1 = [5, 10, 25, 100, 200]
  expected_1 = False
  output_1 = canGetExactChange(target_1, arr_1)
  check(expected_1, output_1)

  target_2 = 75
  arr_2 = [4, 17, 29]
  expected_2 = True
  output_2 = canGetExactChange(target_2, arr_2)
  check(expected_2, output_2)

  # Add your own test cases here
  