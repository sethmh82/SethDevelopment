# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 17:12:17 2021

@author: SethHarden
"""
NO_OF_CHARS = 256

def max_distinct_char(str, n): 
  
    # Initialize all character's 
    # count with 0 
    count = [0] * NO_OF_CHARS 
      
    # Increase the count in array  
    # if a character is found 
    for i in range(n): 
        count[ord(str[i])] += 1
      
    max_distinct = 0
    for i in range(NO_OF_CHARS): 
        if (count[i] != 0): 
            max_distinct += 1    
      
    return max_distinct 
  
def smallesteSubstr_maxDistictChar(str): 
  
    n = len(str)     # size of given string 
  
    # Find maximum distinct characters 
    # in any string 
    max_distinct = max_distinct_char(str, n) 
    minl = n     # result 
      
    # Brute force approach to 
    # find all substrings 
    for i in range(n): 
        for j in range(n): 
            subs = str[i:j] 
            subs_lenght = len(subs) 
            sub_distinct_char = max_distinct_char(subs,  
                                                  subs_lenght) 
              
            # We have to check here both conditions together 
            # 1. substring's distinct characters is equal 
            # to maximum distinct characters 
            # 2. substing's length should be minimum  
            if (subs_lenght < minl and 
                max_distinct == sub_distinct_char): 
                minl = subs_lenght 
  
    return minl 
 
    
def min_length_substring(s, t):

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
  