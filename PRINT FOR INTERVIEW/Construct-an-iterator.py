# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 16:07:19 2021

@author: SethHarden
"""

# OBJECT WITH A STATE THAT REMEMBERS WHERE IT IS DURING ITERATION
class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end  
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current
    
    
def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1
        
        
nums = my_range(1, 5)

for num in nums:
    print(num)