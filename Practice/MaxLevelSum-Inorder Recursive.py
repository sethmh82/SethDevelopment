# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 19:50:37 2021

@author: SethHarden
"""

from collections import defaultdict
class Solution:
    
    def maxLevelSum(self, root: TreeNode) -> int:
        
        def inorder(node, level):
            
            if node:
                
                inorder(node.left, level + 1)
                
                level_sum[level] += node.val
                
                inorder(node.right, level + 1)
            
        level_sum = defaultdict(int)
        
        inorder(root, 1)
        
        return max(level_sum, key = level_sum.get)