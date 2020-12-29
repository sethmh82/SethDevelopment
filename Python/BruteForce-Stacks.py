# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 16:03:28 2020

@author: SethHarden
"""

def bruteforce_solution(arr): #O(N^2)
    # Starts from each index,
    # expand towards both directions looking for a larger element.
    l = len(arr)
    n = [1] * l
    st = []
    for i, x in enumerate(arr):
        for di in [1, -1]:
            step = 1
            while 0 <= i+ di*step < n and  arr[i+ di*step] < x:
                n[i] += 1
                step += 1

    return n



def stack_solution(arr): #O(N)
    # this solution uses Stacks. Every index starts with n possibilities.
    # Using stack, going from left to right, we remove the subarrays that
    # doesn't satisify the problem condition at this line:
    # 'result[st.pop()] -= n-i'
    # Then we do it again from right to left.
    n = len(arr)
    result = [n] * n
    st = []
    for i, x in enumerate(arr):
        while st and x >= arr[st[-1]]:
            result[st.pop()] -= n-i
        st.append(i)
    st.clear()
    for i, x in reversed(list(enumerate(arr))):
        while st and x >= arr[st[-1]]:
            result[st.pop()] -= i+1
        st.append(i)
    return result

import random
arr = [random.randint(1, 100) for _ in range(10)]
print(arr)
print(stack_solution(arr))
print(bruteforce_solution(arr))
assert(stack_solution(arr) == bruteforce_solution(arr))