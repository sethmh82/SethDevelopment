# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 11:24:29 2020

@author: SethHarden

NumPy PYTHON CODE EXAMPLES

NumPy is used to work with Arrays

NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.

This behavior is called locality of reference in computer science.

This is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures.
"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)