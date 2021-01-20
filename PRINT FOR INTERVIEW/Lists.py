# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 18:30:07 2021

@author: SethHarden

Given an array nums of distinct integers, 
return all the possible permutations. 
You can return the answer in any order.

"""

nums = [1,5,4,3]
list = ['a','b','c']

list.append('s')
popped = list.pop()

courses_2 = ['x', 'z']
list.insert(0, courses_2)
list.extend(courses_2)
list.remove(['x','z'])
#print('pop: ',popped)
#print('list: ', list)
list.reverse()
#print('reversed: ', list)
list.sort()
#print('sorted: ', list)
list.sort(reverse=True)
#print('reversed: ', list)
sorted_list = sorted(nums)
#print('nums: ', sorted_list)

#['a','b','c','d','e']

# print(min(nums))
# print(max(nums))
# print(sum(nums))
# return_index = list.index('b')
# print('art' in list)

# for i, list in enumerate(list, start=1):
#     print(i, list)


list_str = ' - '.join(list)
new_list = list_str.split(' - ')
print(list_str)
print(new_list)


1,2,3
1, 
1,2  
1,3
2  
2,3
3
