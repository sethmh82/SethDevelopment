# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 10:49:00 2021

@author: SethHarden
"""

class Solution(object):
    
    def orderlyQueue(string, K):
        if K == 1:
            return min(string[i:] + string[:i] for i in range(len(string)))
        return "".join(sorted(string))
    
    print(orderlyQueue("cba", 1))