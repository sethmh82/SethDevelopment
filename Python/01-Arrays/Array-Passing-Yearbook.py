import math
from collections import defaultdict
# Add any extra import statements you may need here
"""
There are n students
The students are numbered from 1 to n
Each student has their own yearbook.
They are going to pass them around for signing

We are given a list of n integers (our arr)

Student has yearbook
For i in arr:

Is the number of
yearbooks == students

n = 2 #number of students
arr = [2, 1] #the 2 students in an array
output 

What do we know?

length of the array



"""

# Add any helper functions you may need here



#Simplify to O(n*2)
  n = [-1] * len(arr)
  #lets setup another method that considers the student with next student and signatures first
  def countSignature(student: int, next_student: int, signatures: int = 1) -> int:
    if student == next_student:
      return signatures
    return countSignature(student, arr[next_student-1], 1 + signatures)
  
  for i, e in enumerate(arr): #O(n)
    if i == e-1:
      #if they are trying to pass it to themself then assign the index a 1
      n[i] = 1
    else:
      n[i] = countSignature(i+1, arr[i]) 
      #otherwise we increment the index we are passing through
      #this is the equivalent of passing the yearbook for another signature
  return n

"""
  ----------- SOLUTION 2 O(n**2)
  
  length = len(arr) #get our array length
  result = [0] * length #set a list with an index = to that of out original list
  #lets track each yearbook as it makes it way and count how many signtatures
  signatures = set()
  #now lets go through each index of the arr
  for i in range(len(arr)): #O(n)
    if i not in visited: #(n)
      #student who have signed i's yearbook
      student_signing = i
      group_signed = set([i]) 
      #now let's pass the yearbook until it comes back to i 
      #(or i goes into the group_signed set)
      while arr[student_signing]-1 !=i: #the book keeps going until it is returned to owner (i)
        student_signing = arr[student_signing]-1
        group_signed.add(student_signing)
      signatures.update(group_signed)
      #lets go through the signed group, there can only be a max number of signatures in any book.
      #We know a yearbook is fully signed when the group_signed is full (or equal to our "result" length)
      for j in group_signed:
        result[j] = len(group_signed)
  return result
"""

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
  arr_1 = [2, 1]
  expected_1 = [2, 2]
  output_1 = findSignatureCounts(arr_1)
  check(expected_1, output_1)

  arr_2 = [1, 2]
  expected_2 = [1, 1]
  output_2 = findSignatureCounts(arr_2)
  check(expected_2, output_2)


  # Add your own test cases here
  