

"""
LIST QUEUE

      Front:  [][][][][]  :Rear          
   append() >            < appendleft()
  popleft() <            > pop()
 
 queue.append()
 queue.pop(x)
 
 with deque we can
 queue.popleft()
 queue.appendleft()
 
 with Queue
 if queue.empty() =! true
 x = 3
 [1][2][4a][4b]   [5][6]
 
 
 [4a][2][1]
 
 4b == 4a so popleft 4a then append 


then compare [2] to [1] if < append or if > appendleft or pop the collection
if [i] == [i+1] then 
DECREMEMENT and q.popleft and q.appendleft(i)
"""

"""
--------------------------------
WHAT OPERATIONS ARE WE DOING?

Create a list
Adding numbers to that list
Find the highest number and remove it
Decrement all values.
Add them back to the queue

repeat x times
"""
import math
import collections
from collections import deque
from queue import Queue

# Add any extra import statements you may need here

def

def findPositions(arr, x):
    
    
    
    
 """    
    
    ------------------
for (int k = 1; k <= 7; k++) 

q.enqueue(k);
 
for (int k = 1; k <= 4; k++)

 q.enqueue(q.dequeue());
 
 q.dequeue();


def findPositions(arr, x):
    
    arr = [1,3,4,5]
    list = arr
    q = collections.deque()
    arr = deque(list)
    j = x
    z = j
    
    
    while j > 0:
        print("j loop: ", j)
        print("x loop: ", x)
        q.append(arr[0])
        arr.popleft()  
        j -= 1 
        if j == 0:
            break

        
    print("arr: ", arr)
    print("q: ", q)
    
    return arr
            
         

  while x > 0:
        
      for i in q: #loop through the arr
                    #load our first number into the q
                    
        if len(q) == 0 and x > 0: #if we don't have anything in q
            print("Q Adds: [", arr[i], " ]")
            q.enqueue(arr[i]) #send the first number to q
            arr.pop()
            x =- 1
              #if a number is loaded, compare them
              
              
        elif arr[i] == q[0] and x > 0:
            print("Equal, arr Gets Back: [", arr[i], " ]")
                  # just add it back to the array but decrement it
            arr.enqueue(arr[i]-1)
            arr.dequeue()
                  # then delete it from the from the q
            q.dequeue()
            x =- 1
                  #decrement x
              
        elif arr[i] < q[0] and x > 0:
                print("Q is Bigger, ARR Adds: [", arr[i]-1, " ]")
                arr.enqueue(arr[i]-1) 
                  #pop it, decrement, and append it back to arr
                  #now remove the original from the arr
                arr.pop()
                x =- 1
                  #if it is greater than
        elif arr[i] > q[0] and x > 0:
                print("arr is Bigger, Q Gets: [", arr[i], " ]")
    
                arr.enqueue(q.dequeue()-1)
                q.enqueue(arr[i])
                arr.dequeue()
                x =- 1
    
        print(arr)
        print(q)
    
  return arr
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
  n_1 = 6
  x_1 = 5
  arr_1 = [1, 2, 2, 3, 4, 5]
  expected_1 = [5, 6, 4, 1, 2]
  output_1 = findPositions(arr_1, x_1)
  check(expected_1, output_1)
"""
  n_2 = 13
  x_2 = 4
  arr_2 = [2, 4, 2, 4, 3, 1, 2, 2, 3, 4, 3, 4, 4]
  expected_2 = [2, 5, 10, 13]
  output_2 = findPositions(arr_2, x_2)
  check(expected_2, output_2)

  # Add your own test cases here
""" 