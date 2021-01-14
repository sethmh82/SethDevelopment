# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 20:25:00 2021

@author: SethHarden



#LISTS
my_list = [10,20,30,40,50]
for i in my_list:
    print(i)
       
#TUPLES
my_tuples = (1,2,3,4,5,6,7,8,9,10)
for i in my_tup:
    print(i)

#DICTIONARY
my_dict = {'name': 'Bronx', 'age': '2', 'occupation': "Corey's Dog"}
for key,val in my_dict.iteritems():
    print("My {} is {}".format(key,val))    

#SET
my_set = {10,20,30,40,50,10,20,30,40,50}
for i in my_set:
    print(i)

#----------------------------------------------------------------
#LIST COMPREHENSION (and SET)
my_list = [1,2,3,4,5,6,7,8,9,10]
# Give me each number in a list squared
squares = [num*num for num in my_list]
print(squares)
"""
#GENERATORS



   
# FIZZBUZZ

# for num in range(1,101):
#     if num % 5 == 0 and num % 3 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)

     
# FIBONACCI GENERATOR SEQUENCE  

# def fib(num): 
#     a, b = 0,1
#     for i in range(0, num, 1):
#         yield "{}: {}".format(i+1, a)
#         a, b = b, a + b
        
# for item in fib(20):
#     print(item)
        
        
        
        
# FIBONACCI NORMAL SEQUENCE        
# def fib(num): 
#     a, b = 0,1       
#     for i in range(0,num):
#         print(a)
#         a, b = b, a+b
        
     
# fib(100)



#CLASSES
class Person(object):
    def __init__(self, name):
        self.name = name
    
    def reveal_identity(self):
        print ("My name is {}".format(self.name))


class SuperHero(Person):
    def __init__(self, name, hero_name):
        super(SuperHero, self).__init__(name)
        self.hero_name = hero_name
    
    def reveal_identity(self):
        super(SuperHero, self).reveal_identity()
        print("My hero name is {}".format(self.hero_name))





name = Person("seth")
#Person.reveal_identity(name)

hero = SuperHero(name, "batman")
SuperHero.reveal_identity(hero)


Return Type (what we are returning)
Memory 
Operation Usage
Speed












