# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 19:43:58 2021

@author: SethHarden
"""

#  5! = 5*4*3*2*1 = 5*4!
#  4! = 4*3*2*1 = 4*3!
#  3! = 3*2*1 = 3*2!
#  2! = 2*1 = 2*1!
#  1! = 1
#  0! = 1


def recursion(n):
    #print("recurse: ", n)
    if n < 2:
        return 1
    else: 
        return ( n * recursion( n-1 ))
    
print(recursion(20))

def get_recursive_factorial(n):
    if n < 0:
        return -1
    elif n < 2:
        return 1
    else:
        return n * get_recursive_factorial(n-1)
    
def get_iterative_factorial(n):
    if n < 0:
        return -1
    else:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return fact
    
print(get_recursive_factorial(6))
print(get_iterative_factorial(6))