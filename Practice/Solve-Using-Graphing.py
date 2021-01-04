# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 11:42:47 2021

@author: SethHarden
"""

from collections import Counter
class Solution:
    
    
   def solve(self, str1, str2, edges):
       
      possible = len(str1)
      
      #setup our graph its an array for everything in our possible range
      graph = [[] for _ in range(possible)]
      
      
      for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
      matches = 0
      
      seen = [False] * possible
      
      
      for u in range(possible):
          
         if not seen[u]:
            queue = [u]
            seen[u] = True
            
            for x in queue:
                
               for y in graph[x]:
                   
                  if not seen[y]:
                     queue.append(y)
                     seen[y] = True
                     
            count = Counter(str2[i] for i in queue)
            
            for i in queue:
               if count[str1[i]]:
                  count[str1[i]] -= 1      
            matches += 1
            
            
      return matches
  
    
  
    
ob = Solution()
str1 = ["a", "b", "c", "d"]
str2 = ["b", "a", "c", "d"]
C = [[0, 1],[2, 3]]
print(ob.solve(A, B, C))