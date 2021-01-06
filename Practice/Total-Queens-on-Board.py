# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 10:52:46 2021

@author: SethHarden
"""

class Solution:
    def totalNQueens(n):

        def is_not_under_attack(row, col):
            return not (rows[col] or hill[row - col] or dale[row + col])
        
        def place_queen(row, col):
            rows[col] = 1
            hill[row - col] = 1  #slpap up diagnol
            dale[row + col] = 1  #slope down diagnol
        
        def remove_queen(row, col):
            rows[col] = 0
            hill[row - col] = 0 
            dale[row + col] = 0
        
        def backtrack(row = 0, count = 0):
            for col in range(n):
                if is_not_under_attack(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        count += 1
                    else:
                        count = backtrack(row + 1, count)
                    remove_queen(row, col)
            return count
        
        rows = [0] * n
        hill = [0] * (2 * n - 1) 
        dale = [0] * (2 * n - 1) 
        
        return backtrack()
    
    print(totalNQueens(4))