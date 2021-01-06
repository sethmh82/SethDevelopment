# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 16:23:27 2021

@author: SethHarden
"""
class Solution:
    def waysToDistribute(n, k):
        
        table = [[0 for _ in range(n+1)] for _ in range(k+1)]
        print(table)
        modulo = 10 ** 9 + 7 #returns it shortened 10^9 + 7
        
        for i in range(k+1):
            table[i][i] = 1
            
        for i in range(1, k+1):
            for j in range(i+1, n+1):
                table[i][j] = (i * table[i][j-1] + table[i-1][j-1]) % modulo
                
        return table[k][n]
    
    
    if __name__ == "__main__":
        candies = 20
        bags = 5
        print(waysToDistribute(candies, bags))