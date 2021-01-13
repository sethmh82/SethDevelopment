# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 12:53:34 2021

@author: SethHarden
"""

# ENUMERATE 

grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)


# converting to list
print(list(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery, 5)
print(list(enumerateGrocery))

'''
number = [1, 2, 3]
print(dir(number))

print('\nReturn Value from empty dir()')
print(dir())

# keyword argument is not passed
numbers1 = dict([('x', 5), ('y', -5)])
print('numbers1 =',numbers1)

# keyword argument is also passed
numbers2 = dict([('x', 5), ('y', -5)], z=8)
print('numbers2 =',numbers2)

# zip() creates an iterable in Python 3
numbers3 = dict(dict(zip(['x', 'y', 'z'], [1, 2, 3])))
print('numbers3 =',numbers3)

numbers1 = {'y': -5, 'x': 5}
'''

'''
num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lambda n1, n2: n1+n2, num1, num2)
print(list(result))




numbers = (1, 2, 3, 4)
out = map(lambda x: x*x, numbers)
print(out)

# converting map object to set
numbersSquare = set(out)
print(numbersSquare)



print("-------------------------------------------------------------")

def calculateSquare(n):
    return n*n


numbers = (2, 4)
result = map(calculateSquare, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)
'''