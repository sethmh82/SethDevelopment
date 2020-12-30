# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 10:23:31 2020

@author: SethHarden


GENERAL PYTHON CODE EXAMPLES
"""

print("-------------------- DICTIONARY --------------------")
# dict()
# --------------------------------------------------
# The dict() function creates a dictionary.
# A dictionary is a collection which is unordered, changeable and indexed.
    
x = dict(name = "John", age = 36, country = "Norway")


thisdict = {
  "brand": "Gateway",
  "model": "P5-75",
  "year": 1996,
  "sold": 578543,
  "colors": ["black", "white", "green"]
}

"""
print(thisdict) #print entire dictionary
print(thisdict["brand"]) #just the brand
print(len(thisdict)) #number of entries in dictionary
print(type(thisdict)) #prints <class 'dict'>
print(thisdict.get("sold")) #returns the value of sold
print(thisdict.keys()) #returns a list of all keys (['brand', 'model', 'year', 'sold', 'colors'])

# CHANGE / ADD
print("Before: ", thisdict["brand"], thisdict.keys())
thisdict["brand"] = "Apple"
thisdict["os"] = "macOS"
print("After: ", thisdict["brand"], thisdict.keys())
"""

# LOOP
print("-- MAIN --")
for x in thisdict:
    print(x)
print("-- VALUE V1 --")    
for x in thisdict:
    print(thisdict[x])
print("-- VALUE V2 --")
#returns the values
for x in thisdict.values():
  print(x)
print("-- KEYS --")
#keys() returns the key
for x in thisdict.keys():
  print(x)
print("-- ITEMS --")
# items() both keys and values
for x, y in thisdict.items():
  print(x, y)
  
  

"""
# REMOVE / CLEAR / DELETE
thisdict.popitem() #this removes the last item which is "os"

thisdict.pop("colors") #removed the color entry
print(thisdict)

del thisdict["sold"] #delete sold
thisdict.clear() #clears it
del thisdict #delete entire reference of thisdict












print("-------------------- TUPLES --------------------")
# Tuples
# --------------------------------------------------
# uple items are ordered, unchangeable, and allow duplicate values.

thistuple = ("apple", "banana", "cherry")
print(thistuple)


print("---------- LAMBDA ----------")
# Lambda
# --------------------------------------------------
# A small anonymous function
x = lambda a : a + 10
print(x(5)) #15

x = lambda a, b : a * b
print(x(5, 6)) #30

x = lambda a, b, c : a + b + c
print(x(5, 6, 2)) #13

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) #22
print(mytripler(11)) #33


# dict()
# --------------------------------------------------
# C


# dict()
# --------------------------------------------------
# C
"""