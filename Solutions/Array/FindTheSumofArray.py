# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 17:39:10 2020

@author: SethHarden
"""




def find_sum(arr):
    total = 0
    for i in arr:
        total += i
    return total

arr = [1, 4, 3, 2, 6]
print(find_sum(arr))