# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 15:17:30 2021

@author: SethHarden
"""
#linear runtime because we go character by character
#if you call upper it has to create a new string (because they are immutable)
def case_insensitive_compare(s1, s2):
    
    if len(s1) != len(s2):
        return False
    s1_iter = iter(s1)
    s2_iter = iter(s2) 
    for _ in range(len(s1)):
        s1_c = next(s1_iter)
        s2_c = next(s2_iter)
        if not s1_c.upper() == s2_c.upper():
            return False
    return True

def insert_delete_compare(s1, s2, tolerance):
    if len(s1) != len(s2):
        if abs(len(s1) - len(s2)) == 1:
            shorter, longer = sorted([s1, s2], key=len)
        else:
            return False
    else:
        return case_insensitive_compare(s1, s2)
    shorter_iter = iter(shorter)
    longer_iter = iter(longer)
    
    
    for _ in range(len(shorter)):
        shorter_c = next(shorter_iter)
        longer_c = next(longer_iter)
        if not longer_c.upper() == shorter_c.upper():
            next_longer = next(longer_iter)
            if not next_longer.upper() == shorter_c.upper():
                return False
    return True
    


print (insert_delete_compare('abc', 'ABC'))

print (insert_delete_compare('azy', 'ABCa'))

print (insert_delete_compare('azy', 'ABCa'))


