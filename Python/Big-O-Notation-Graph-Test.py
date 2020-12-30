# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 08:29:28 2020

@author: SethHarden
"""

import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
plt.style.use('bmh')

#set up runtime comparisons
n = np.linspace(1,10)

labels = ['Constant', 'logarithmic', 'Linear', 'Log Linear', 'Quadratic', 'Cubic', 'Exponential']
big_o = [np.ones(n.shape), np.log(n), n, n*np.log(n), n**2, n**3, 2**n]

plt.figure(figsize=(12,10))
plt.ylim(0,50)

for i in range(len(big_o)):
    plt.plot(n,big_o[i], label=labels[i])
    
plt.legend(loc=0)
plt.ylabel('Relative Runtime')
plt.xlabel('n')