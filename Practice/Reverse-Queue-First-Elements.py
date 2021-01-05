# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 18:22:34 2021

@author: SethHarden
"""

from queue import Queue 
from collections import deque
  
# Function to reverse the first K  
# elements of the Queue  
def reverseQueueFirstKElements(x, arr): 
    if (arr.empty() == True or
             x > arr.qsize()):  
        return
    if (x <= 0):  
        return
  
    Stack = [] 
  
    # put the first K elements  
    # into a Stack 
    for i in range(x): 
        print("Ad to stack: ", arr.queue[0])
        Stack.append(arr.queue[0])  
        arr.get() 
        print(Stack)
  
    # Enqueue the contents of stack  
    # at the back of the queue 
    print(Stack)
    while (len(Stack) != 0 ):  
        print("Back to queue: ", Stack[-1])
        arr.put(Stack[-1])  
        Stack.pop() 
  
    # Remove the remaining elements and  
    # enqueue them at the end of the Queue 
    for i in range(arr.qsize() - x): 
        print("Remove and Requeue: ", arr.queue[0])
        arr.put(arr.queue[0])  
        arr.get() 
        
    return arr
 
    
 
# Utility Function to print the Queue  
def Print(arr): 
    while (not arr.empty()):  
        print(arr.queue[0], ", ", end =" ")  
        arr.get() 
  
    
def findPositions(arr, x):

    Print(reverseQueueFirstKElements(x, arr))
    print("Expected: [5, 6, 4, 2, 1]")
    
  



if __name__ == "__main__":
    arr = Queue()  
    arr.put(1)  
    arr.put(2)  
    arr.put(2)  
    arr.put(3)  
    arr.put(4)  
    arr.put(5)

    

    x = 5
    #arr_1 = [1, 2, 2, 3, 4, 5]
    #expected_1 = [5, 6, 4, 1, 2]
    output_1 = findPositions(arr, x)

  
"""  
    n_2 = 13
    x_2 = 4
    arr_2 = [2, 4, 2, 4, 3, 1, 2, 2, 3, 4, 3, 4, 4]
    expected_2 = [2, 5, 10, 13]
    output_2 = findPositions(arr_2, x_2)
    check(expected_2, output_2)
  
    # Add your own test cases here
    

    Queue = Queue()  
    Queue.put(10)  
    Queue.put(20)  
    Queue.put(30)  
    Queue.put(40)  
    Queue.put(50)  
    Queue.put(60)  
    Queue.put(70)  
    Queue.put(80)  
    Queue.put(90)  
    Queue.put(100)  
      
    k = 5
    reverseQueueFirstKElements(k, Queue)  
    Print(Queue) 
    
"""