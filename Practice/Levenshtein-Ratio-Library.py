# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 15:59:55 2021

@author: SethHarden
"""

import Levenshtein as lev



Str1 = "Apple Inc."
Str2 = "apple Inc"
Distance = lev.distance(Str1.lower(),Str2.lower()),
print(Distance)
Ratio = lev.ratio(Str1.lower(),Str2.lower())
print(Ratio)