# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 16:50:19 2020

@author: SethHarden
"""

        
        
 # Python3 program to find averages of  
# all levels in a binary tree.  
  
# Importing Queue 
from queue import Queue 
  
# Helper class that allocates a  
# new node with the given data and  
# None left and right pointers.  
class newNode: 
    def __init__(self, data): 
        self.val = data  
        self.left = self.right = None
      
# Function to print the average value  
# of the nodes on each level  
def averageOfLevels(root): 
  
    # Traversing level by level  
    q = Queue() 
    q.put(root)  
    while (not q.empty()): 
  
        # Compute Sum of nodes and  
        # count of nodes in current  
        # level.  
        Sum = 0
        count = 0
        temp = Queue()  
        while (not q.empty()):  
            n = q.queue[0]  
            q.get()  
            Sum += n.val  
            count += 1
            if (n.left != None): 
                temp.put(n.left)  
            if (n.right != None):  
                temp.put(n.right) 
        q = temp  
        print((Sum * 1.0 / count), end = " ") 
  
# Driver code  
if __name__ == '__main__': 
  
    # Let us construct a Binary Tree  
    #     4  
    # / \  
    # 2 9  
    # / \ \  
    # 3 5 7  
    root = None
    root = newNode(4)  
    root.left = newNode(2)  
    root.right = newNode(9)  
    root.left.left = newNode(3)  
    root.left.right = newNode(8)  
    root.right.right = newNode(7)  
    averageOfLevels(root) 
  
# This code is contributed by PranchalK 