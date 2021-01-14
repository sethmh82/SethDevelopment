# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 12:53:34 2021

@author: SethHarden
"""
class Mammal(object):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    
class Dog(Mammal):
  def __init__(self):
    print('Dog has four legs.')
    
    super().__init__('Dog')
    
d1 = Dog()



'''
# ZIP TUPLES
numbersList = [1, 2, 3]
str_list = ['one', 'two']
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')

# Notice, the size of numbersList and numbers_tuple is different
result = zip(numbersList, numbers_tuple)

# Converting to set
result_set = set(result)
print(result_set)

result = zip(numbersList, str_list, numbers_tuple)

# Converting to set
result_set = set(result)
print(result_set)


print("-------------------------------------------------------------")


x = 7
y = 3
z = 5

print(pow(x, y, z))




square = {2: 4, -3: 9, -1: 1, -2: 4}

# the largest key
key1 = max(square)
print("The largest key:", key1)    # 2

# the key whose value is the largest
key2 = max(square, key = lambda k: square[k])

print("The key with the largest value:", key2)    # -3

# getting the largest value
print("The largest value:", square[key2])    # 9




# FILTER 
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filterVowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(letter in vowels):
        return True
    else:
        return False

filteredVowels = filter(filterVowels, letters)

print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)
    
    
'''

'''
# ENUMERATE 

grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)


# converting to list
print(list(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery, 5)
print(list(enumerateGrocery))
'''

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