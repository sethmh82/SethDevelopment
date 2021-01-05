# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 13:55:14 2021

@author: SethHarden

we just need the sum and 
4
7 9
10 2 6
6
2


data: {0:[4], 1:[7,9], 2:[10, 2, 6], 3:[6], 4:[2]}
data: (0: (4,1), 1: (16, 2), )

result: [4, 8, 6, 6, 2]
"""

class node(object):
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None
        
        
    #this gives us a node with no values.
    
    
    
    
def _collect(node, data, depth = 0):
    if not node:
        return None
    if depth not in data:
        data[depth] = (node.val, 1)
    else:
        val, count = data[depth]
        val += node.val
        count += 1
        data[depth] = (val, count)
        
    _collect(node.left, data, depth + 1)
    _collect(node.left, data, depth + 1)


def avg_by_depth(node):
    data = {}
    _collect(node, data)
    result = []
    i = 0 
    while i in data:
        val, count = data[i]
        nums = data[i] 
        avg = sum(nums) / len(nums)
        result.append(val / count)
        i += 1
        
    return results
