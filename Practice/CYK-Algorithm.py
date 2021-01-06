# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 15:30:12 2021

@author: SethHarden

Cocke–Younger–Kasami
or
CYK Algorithm
"""

# Python implementation for the 
# CYK Algorithm 
import math
# Non-terminal symbols 

non_terminals = ["A", "B", "C", "D", "E", "F"] 

terminals = ["book", "orange", "man", "tall", "heavy", "very", "muscular"] 
  
# Rules of the grammar 
rules = {
     "A": [["C", "B"]], 
     "B": [["D", "B"], ["book"], ["orange"], ["man"]], 
     "D": [["E", "A"], ["heavy"], ["orange"], ["tall"]], 
     "C": [["a"]], 
     "E": [["very"], ["extremely"]], 
     "F": [["heavy"], ["orange"], ["tall"], ["muscular"]] 
    } 
  
# Function to perform the CYK Algorithm 
def cykParse(string): 
    
    n = len(string) #get the length
    
    # this is how you construct a table
    T = [[set([]) for j in range(n)] for i in range(n)] # Initialize the table

    for j in range(0, n): # Filling in the table 
        print("j: ", j)
        for lhs, rule in rules.items(): # Iterate over the rules 
            
            for i_rule in rule: 
                # If a terminal is found 
                if len(i_rule) == 1 and \
                i_rule[0] == string[j]:
                    T[j][j].add(lhs)
                    print("lhs: ", lhs)
                    
        for i in range(j, -1, -1):
            for k in range(i, j + 1):# Iterate over the range i to j + 1  
                for lhs, rule in rules.items(): # Iterate over the rules 
                    for i_rule in rule:
                        # If a terminal is found 
                        # print(i_rule[0], " : ", T[i])
                        
                        if len(i_rule) == 2 and \
                        i_rule[0] in T[i][k] and \
                        i_rule[1] in T[k + 1][j]: 
                            T[i][j].add(lhs) 
                            
# If word can be formed by rules of given grammar 

    if len(T[0][n-1]) != 0: 
        print("True") 
    else: 
        print("False") 
        
        
# Driver Code 
# Given string 
string = "a very heavy orange book".split() 
#converts this to ['a', 'very', 'heavy', 'orange', 'book']
  
# Function Call 
cykParse(string) 