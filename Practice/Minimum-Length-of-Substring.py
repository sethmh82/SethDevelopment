# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 16:04:06 2021

@author: SethHarden
"""

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here
  
  
  # Lets do this for case 1
  # s = "dcbefebce"
  # t = "fd"
  
  

def min_length_substring(s, t):
  # Write your code here
  # collect string s
  string_name = s
  select_substring = t
  # collect string t
  # store the index for comparison
  high = 0
  low = 0
  
  foundstring = ("")

  # search string s
  for i, v in enumerate(select_substring):
    #print("i: ", i)
    print("v: ", v)
    
    for j, z in enumerate(string_name):
      #print("j: ", j)
      print("z: ", z)
      
      if z == v:
          print("found: ", z, "at index: ", j)

          foundstring += z
          #determine if it is the highest or lowest index.
          if j > high and j > low:
            high = j
            break
          elif j <= low and j < high:
            low = j
            break
  

  if foundstring == t:
      print("High: ", high, " Low: ", low)
      print("MATCH")

      return (len(s) - (high - low))
  else:
      print("High: ", high, " Low: ", low)
      print("strings do not match")
      print("found: ", foundstring)
      print("orig: ", t)
      return -1
      
  # count substring
  # return either a # or a -1
	


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 2

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

  s1 = "dcbefebce"
  t1 = "fd"
  expected_1 = 5
  output_1 = min_length_substring(s1, t1)
  check(expected_1, output_1)
  

  s2 = "xakljdklblskjdflkdjclskfjls"
  t2 = "abc"
  expected_2 = -1
  output_2 = min_length_substring(s2, t2)
  check(expected_2, output_2)

	# Add your own test cases here
  