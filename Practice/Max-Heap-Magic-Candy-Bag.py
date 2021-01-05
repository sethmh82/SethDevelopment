# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 13:53:28 2021

@author: SethHarden
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 17:47:29 2021

@author: SethHarden
"""
import sys 
  
# class MaxHeap: 
  
def __init__(maxsize): 
      
    maxsize = maxsize 
    size = 0
    Heap = [0] * (maxsize + 1) 
    Heap[0] = sys.maxsize 
    FRONT = 1


# Function to return the position of 
# parent for the node currently 
# at pos 
def parent(pos): 
      
    return pos // 2
  
# Function to return the position of 
# the left child for the node currently 
# at pos 
def leftChild(pos): 
      
    return 2 * pos 
  
# Function to return the position of 
# the right child for the node currently 
# at pos 
def rightChild(pos): 
      
    return (2 * pos) + 1
  
# Function that returns true if the passed 
# node is a leaf node 
def isLeaf(pos): 
      
    if pos >= (size//2) and pos <= size: 
        return True
    return False
  
# Function to swap two nodes of the heap 
def swap(fpos, spos): 
      
    Heap[fpos], Heap[spos] = (Heap[spos],  
                                        Heap[fpos]) 
  
# Function to heapify the node at pos 
def maxHeapify(pos): 
  
    # If the node is a non-leaf node and smaller 
    # than any of its child 
    if not isLeaf(pos): 
        if (Heap[pos] < Heap[leftChild(pos)] or
            Heap[pos] < Heap[rightChild(pos)]): 
  
            # Swap with the left child and heapify 
            # the left child 
            if (Heap[leftChild(pos)] >  
                Heap[rightChild(pos)]): 
                swap(pos, leftChild(pos)) 
                maxHeapify(leftChild(pos)) 
  
            # Swap with the right child and heapify 
            # the right child 
            else: 
                swap(pos, rightChild(pos)) 
                maxHeapify(rightChild(pos)) 
  
# Function to insert a node into the heap 
def insert(element): 
      
    if size >= maxsize: 
        return
    size += 1
    Heap[size] = element 
  
    current = size 
  
    while (Heap[current] >  
           Heap[parent(current)]): 
        swap(current, parent(current)) 
        current = parent(current) 
  
# Function to print the contents of the heap 
def Print(self): 
      
    for i in range(1, (size // 2) + 1):
        
        print(" PARENT NODE: " + str(Heap[i]) + 
              " LEFT CHILD : " + str(Heap[2 * i]) +
              " RIGHT CHILD : " + str(Heap[2 * i + 1])) 
  
# Function to remove and return the maximum 
# element from the heap 
def extractMax(self): 
  
    popped = Heap[FRONT] 
    Heap[FRONT] = Heap[size] 
    size -= 1
    maxHeapify(FRONT) 
      
    return popped 

def maxCandies(arr, k):
  # Write your code here
  
    bags = arr.sort(reverse=True) # [1 2 2 4 7]
    opens = k
    
    maxHeap = MaxHeap(opens) # we will only store 5 elements
    
    for i in range(opens):
      if bags[i] <= bags[i-1]//2:
          print("Inserted: ", (bags[i-1]//2))
          maxHeap.insert(bags[i-1]//2)
      else: 
          maxHeap.insert(bags[i])
          print("Inserted: ", (bags[i-1]//2))
     
        
    # now our heap is 
  
# Driver Code 
if __name__ == "__main__": 
      
    
    k = 3
    arr = [2, 1, 7, 4, 2]
    
    maxHeap = MaxHeap(3)
    print(maxCandies(arr, k))
    
    
    
"""    
    print('The maxHeap is ') 
      
    maxHeap = MaxHeap(11) 
    
    maxHeap.insert(7) 
    maxHeap.insert(4) 
    maxHeap.insert(3) 
    maxHeap.insert(2) 
    maxHeap.insert(2) 
    maxHeap.insert(2) 
    maxHeap.insert(1) 
    maxHeap.insert(1) 
    maxHeap.insert(1) 
    maxHeap.insert(1)
    maxHeap.insert(1) 

        


    
    maxHeap.Print() 
      
print('MAX: ', maxHeap.extractMax())
    
  
    maxHeap.insert(3) 
    maxHeap.insert(1)
    
    maxHeap.insert(4)
    maxHeap.insert(2)
    maxHeap.insert(1)
    
    maxHeap.insert(2)
    maxHeap.insert(1)
    
    maxHeap.insert(2)
    maxHeap.insert(1)

                     7
                  /    \
                 4      3
               /  \    / \ 
               2   2   2  1 
             / \   / \
             1  1  1 1  



 
    maxHeap.insert(7) 
    maxHeap.insert(3)

    maxHeap.insert(1) 
    maxHeap.insert(2) 
    maxHeap.insert(1) 
    
    maxHeap.insert(3) 
    maxHeap.insert(2) 
    maxHeap.insert(1) 
    
    maxHeap.insert(4) 
    maxHeap.insert(2) 
    maxHeap.insert(1) 
    maxHeap.insert(2) 
    maxHeap.insert(1) 
"""    
    
