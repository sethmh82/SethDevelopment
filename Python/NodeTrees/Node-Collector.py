# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 17:14:40 2020

@author: SethHarden
"""

class Node(object):
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None
        
def _collect(node, data, depth = 0):
    if not node:
        return None
    
    if depth not in data:
        data[depth] = []
        
    data[depth].append(node.val)
    
    _collection(node.left, data, depth +1)
    