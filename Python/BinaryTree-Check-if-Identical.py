# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 09:21:23 2020

@author: SethHarden
"""


""" VERSION 1 ITERATIVE
# Data structure to store a Binary Tree node
class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 
 
# Recursive function to check if two given binary trees are identical or not
def isIdentical(x, y):
 
    # if both trees are empty, return true
    if x is None and y is None:
        return True
 
    # if both trees are non-empty and value of their root node matches,
    # recur for their left and right sub-tree
    return (x and y) and (x.key == y.key) and \
           isIdentical(x.left, y.left) and isIdentical(x.right, y.right)
 
 
if __name__ == '__main__':
 
    # construct first tree
    x = Node(15)
    x.left = Node(10)
    x.right = Node(20)
    x.left.left = Node(8)
    x.left.right = Node(12)
    x.right.left = Node(16)
    x.right.right = Node(25)
 
    # construct second tree
    y = Node(15)
    y.left = Node(10)
    y.right = Node(20)
    y.left.left = Node(8)
    y.left.right = Node(12)
    y.right.left = Node(16)
    y.right.right = Node(25)
 
    if isIdentical(x, y):
        print("Given Binary Trees are identical")
    else:
        print("Given Binary Trees are not identical")
     
        
     
        
     ------------ VERSION 2 RECURSIVE --------------
"""        
        
from collections import deque
 
 
# Data structure to store a Binary Tree node
class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 
 
# Iterative function to check if two given binary trees are identical or not
def isIdentical(x, y):
 
    # if both trees are empty, return true
    if x is None and y is None:
        return True
 
    # if first tree is empty (& second tree is non-empty), return false
    if x is None:
        return False
 
    # if second tree is empty (& first tree is non-empty), return false
    if y is None:
        return False
 
    # create a stack to hold pairs
    stack = deque()
    stack.append((x, y))
 
    # loop till stack is empty
    while stack:
        # pop top pair from the stack and process it
        x, y = stack.pop()
 
        # if value of their root node don't match, return false
        if x.key != y.key:
            return False
 
        # if left subtree of both x and y exists, push their addresses
        # to stack else return false if only one left child exists
        if x.left and y.left:
            stack.append((x.left, y.left))
        elif x.left or y.left:
            return False
 
        # if right subtree of both x and y exists, push their addresses
        # to stack else return false if only one right child exists
        if x.right and y.right:
            stack.append((x.right, y.right))
        elif x.right or y.right:
            return False
 
    # if we reach here, both binary trees are identical
    return True
 
 
if __name__ == '__main__':
 
    # construct first tree
    x = Node(15)
    x.left = Node(10)
    x.right = Node(20)
    x.left.left = Node(8)
    x.left.right = Node(12)
    x.right.left = Node(16)
    x.right.right = Node(25)
 
    # construct second tree
    y = Node(15)
    y.left = Node(10)
    y.right = Node(20)
    y.left.left = Node(8)
    y.left.right = Node(12)
    y.right.left = Node(16)
    y.right.right = Node(25)
 
    if isIdentical(x, y):
        print("Given binary Trees are identical")
    else:
        print("Given binary Trees are not identical")
 