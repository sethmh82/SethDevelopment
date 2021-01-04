# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 18:10:42 2021

@author: SethHarden
"""
def heapify(bags, totalbags, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < totalbags and bags[largest] < bags[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < totalbags and bags[largest] < bags[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        bags[i], bags[largest] = bags[largest], bags[i]  # swap
 
        # Heapify the root.
        heapify(bags, totalbags, largest)
 
# The main function to sort an array of given size
 
 
def heapSort(bags):
    totalbags = len(bags)
 
    # Build a maxheap.
    for i in range(totalbags//2 - 1, -1, -1):
        heapify(bags, totalbags, i)
 
    # One by one extract elements
    for i in range(totalbags-1, 0, -1):
        bags[i], bags[0] = bags[0], bags[i]  # swap
        heapify(bags, i, 0)
 
def maxCandies(bags, k)
    #examine the k value and k-1 value of the max array
    #lets add their magic values
    #for each in bags add (k//2
    #[7, 4, 2]
    
    # while bags(i)
    #for each value we will //2 until the value is 0
    #start at bags[0]
    
    
# Driver code
bags = [2, 1, 7, 4, 2]
keys = 3
heapSort(bags)
totalbags = len(bags)
print (heapSort(bags))
print("Sorted array is")
for i in range(totalbags):
    print("%d" % bags[i]),