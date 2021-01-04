# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 09:00:31 2021

@author: SethHarden
"""

import math

from collections import Counter


def swapChar(c, i, j):
    c = list(c)
    c[i], c[j] = c[j], c[i]
    #print(''.join(c))
    return ''.join(c)


    
    
def matching_pairs(s, t):
    
  
 
    
    str1 = s
    str2 = swapChar(t, 0, len(t)-1)
    
    c = 0; j = 0;  
  
    # Traverse the string 1 char by char  
    for i in range(len(str1)): 

        if str1[i] in str2 : 
            
            if str1.index(str1[i]) == str2.index(str1[i]):
                c += 1;  
        j += 1;  
        

    print("C: ", c, "J:", j, " Max: ", len(str1))
    return (float(j)/float(c))
    #return (c+j)





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
    

  s_1, t_1 = "abcde", "adcbe"
  expected_1 = 5
  output_1 = matching_pairs(s_1, t_1)
  check(expected_1, output_1)

  s_2, t_2 = "abcd", "abcd"
  expected_2 = 2
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)

  s_3, t_3 = "mno", "mno"
  expected_3 = 1
  output_3 = matching_pairs(s_3, t_3)
  check(expected_3, output_3)
  # Add your own test cases here
  
  s_4, t_4 = "abcd", "adcb"
  expected_4 = 4
  output_4 = matching_pairs(s_4, t_4)
  check(expected_4, output_4)
  # Add your own test cases here
  