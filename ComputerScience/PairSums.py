# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 16:58:53 2020

@author: SethHarden
"""

def numberOfWays(arr, k):
  if not arr: #lets make it safe and check for the correct object name
    return 0
  hashtable = {} #setup a hash table
  n = 0 #assign 0 to n (our counter)
  for i in arr: #lets move in order through each number
    dif = int(k) - int(i) #assign the difference to dif
    if i in hashtable: #if the index or our array is in the hashtable
      n += hashtable[i] #the current count plus the current hashtable index 
      hashtable[i] += 1 #the current hastable index plus 1
    else:
      hashtable[dif] = 1 #whatever index the dif is at gets a 1
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
  k_1 = 6
  arr_1 = [1, 2, 3, 4, 3]
  expected_1 = 2
  output_1 = numberOfWays(arr_1, k_1)
  check(expected_1, output_1)
  
  k_2 = 6
  arr_2 = [1, 5, 3, 3, 3]
  expected_2 = 4
  output_2 = numberOfWays(arr_2, k_2)
  check(expected_2, output_2)

  # Add your own test cases here  
  k_3 = 9
  arr_3 = [5, 3, 5, 3, 4, 5, 9] 
  print(numberOfWays(arr_3, k_3))
