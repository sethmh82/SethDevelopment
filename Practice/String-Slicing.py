# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 09:43:06 2021

@author: SethHarden
"""

# SLICING ------------------------------------------------
x = 'computer'

#[start : end : step]
print(x[1:6:2])
print(x[1:4]) #1 - 4
print(x[3:]) #3 - end
print(x[:5]) #0 - 5

print(x[-1]) #gets from right side
print(x[:-2]) #from 0 until the last 2

print('-----------------------------------------')

# ADDING / CONCATENATING

# STRING 
x = 'horse' + 'shoe'
print(x)

# LIST
y = ['pig', 'cow'] + ['horse']

#TUPLE
z = ('DoubleDz', 'Seth', 'Aroosh') + ('RickD',) + ('Anshul',)
                                     #NEEDS THE COMMA , !!!
print(z)
print('-----------------------------------------')

# CHECKING MEMBERSHIP

x = 'bug'
print ('u' in x)

# LIST

