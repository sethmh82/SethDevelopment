# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 10:33:16 2021

@author: SethHarden

Simple example of Factoral Recursion
"""

def factorial_recursive(n):
    # Stop when you hit 1
    if n == 1:
        print("n: ", n)
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        print("n: ", n)
        return n * factorial_recursive(n-1)
    
print(factorial_recursive(8))