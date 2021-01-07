# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 10:45:22 2021

@author: SethHarden
"""
import math
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
           
class Solution:
    def isValidBST(self, root):
        
        def validate(node, low =- math.inf, high = math.inf):
            print(node)
            #if there is no node 
            if not node:
                return True
            
            if node.val <= low or node.val >= high:

                return False
            
            #RECURSIVE validation
            return (validate(node.right, node.val, high) and validate(node.left, low, node.val))
        
        return validate(root)




if __name__ == "__main__":
    s = [2,1,3,6,7,9,4]
    x = TreeNode()
    y = Solution()
    print(y.isValidBST(x.__init__(s)))