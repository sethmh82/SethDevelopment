# TWO SUM
'''
Given an array of integers (nums) and an integer (taget).
Visualize the inputs:     nums = [2,7,11,15]    target = 9
'''
# One-pass Hash Table
# This is O(n) / O(1)
def twoSum(numbers, target):
    
    dictionary = {}
    
    for index, value in enumerate(numbers):
        complement = target - value

        if complement not in dictionary:
            dictionary[value] = index

        else:
            return [dictionary[complement], index]
        
    return "None found"
                 

numbers = [1,2,6,7,11,15]
target = 9
print(Solution.twoSum(numbers, target))



                


