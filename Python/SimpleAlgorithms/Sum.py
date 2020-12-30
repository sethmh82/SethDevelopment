# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 16:42:50 2020

@author: SethHarden
"""


def sum1(n):
    final_sum = 0
    for x in range(n+1): #only 1 assignment here
        final_sum += x
        
    return final_sum


def sum2(n):
    return (n*(n+1))/2


def sum3(n):
    final_sum = 0
    for x in range(n+1):
        for y in range(n+1):
            final_sum += y
            
    return final_sum       
            
# %timeit sum1(10)