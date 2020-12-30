# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 08:40:27 2020

@author: SethHarden


Big 0 Examples
O(1) CONSTANT TIME
"""

def func_constant(values):
    print (values[0])

# it doesnt matter how long our list becomes
print("--- O(1) CONSTANT ---")
func_constant([1,2,3])

"""
O(1) VERSION 2
"""
def func_constant2(a, b):
    if a > b:
        print("True")
        return True
    else:
        print("False")
        return False
func_constant2(5,3)

"""
O(n) LINEAR TIME
"""

def func_lin(lst):
    for val in lst:
        print (val)
#as the list grows so does the computation value
print("--- O(n) LINEAR ---")
func_lin([1,2,3])

"""
O(log n) LOGARITHMIC TIME
"""
def binary_search(data, value):
    n = len(data)
    left = 0
    right = n - 1
    #we split the input up and lower the size of our input.
    while left <= right:
        middle = (left + right) // 2
        if value < data[middle]:
            left = middle + 1
        else:
            return middle
    raise ValueError('Value is not in the list')
    
print("--- O(log n) LOGARITHMIC TIME ---")   
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(data,8))

"""
O(n^2) QUADRATIC TIME
"""

def func_quad(lst):
    
    for item_1 in lst:
        for item_2 in lst:
            print (item_1, item_2)
            
lst = [1, 2, 3]
print("--- O(n^2) QUADRATIC ---")
func_quad(lst)



def BigO(n):
    return (45*n**3) + (20*n**2 + 19)
    # (n**3) is the most significant term
print("--- CALCULATIONS ---")
print(BigO(10))