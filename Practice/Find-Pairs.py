# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 12:49:10 2021

@author: SethHarden
"""

def find_pairs(arr, target):
    # any comparison 
    dictionary = {}
    
    # loop through the array
    for i in arr:
        # if that array value is not in the dictionary
        
        if i in dictionary:
            # increment the dictionary index by 1
            dictionary[i] += 1
        else:
            # increment the dictionary index by 2
            dictionary[i] = 0
 
    for i in arr:
        complementary = target - i
        
        if complementary in dictionary:
            if complementary == i:
                if not dictionary[complementary] > 0:
                    continue
            
            return str(i) + " and " + str(complementary)
    return "No valid pairs"
    


print(find_pairs([14, 13, 6, 7, 8, 10, 1, 2], 3) == "1 and 2")
print(find_pairs([14, 13, 6, 7, 8, 10, 1], 3) == "No valid pairs")
print(find_pairs([2,2], 4) == "2 and 2")
print(find_pairs([2], 4) == "No valid pairs")
print(find_pairs([1, -3], -2) == "1 and -3")
print(find_pairs([-1, -3, 1, 3], -4) == "-1 and -3")
print(find_pairs([], 4) == "No valid pairs")