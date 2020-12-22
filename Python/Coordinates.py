# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

print("Hello world")

print(random.randint(16, 272))
print("-------------------")


class Coordinate (object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"
        
c = Coordinate(10,10)
zero = Coordinate (0,0)

print(c.distance(zero))

""" 
OR
"""

print(Coordinate.distance(c, zero))
print(c)
print(type(c))
print(type(Coordinate))
print(isinstance(c, Coordinate))


__init__(self, num, denom):
__add__(self, other)
__sub__(self, other)