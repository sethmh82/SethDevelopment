# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 16:42:03 2021

@author: SethHarden
"""

class Person():
    pass

person = Person()

person_info = {'first': 'Corey', 'last': 'Schafer'}

for key, value in person_info.items():
    setattr(person, key, value)
    
print(person.first)
print(person.last)

for key in person_info.keys():
    print(getattr(person,key))