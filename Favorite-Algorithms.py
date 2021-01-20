#LENGTH OF LONGEST SUBSTRING
    def lengthOfLongestSubstring(self, letters: str) -> int:
        
        #assign total length of letters
        total_length = len(letters)
        
        # set a minimum to our answer
        answer = 0
        
        # value_index will store each character once, and its max index
        value_index = {}

        index = 0
        # try to extend the range [i, j]
        for letter in range(total_length):
            
            if letters[letter] in value_index:
                
                index = max(value_index[letters[letter]], index)

                
            answer = max(answer, letter - index + 1)
            
            value_index[letters[letter]] = letter + 1

        return answer
    
if __name__ == "__main__":
    
    s = "eabcabcbbne"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))


"""
MERGE ARRAYS
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #make a copy but just the beginning to m
        nums1_copy = nums1[:m] 
        #empty nums1
        nums1[:] = []

        # Two get pointers for nums1_copy and nums2.
        p1 = 0 
        p2 = 0
        
        # Compare elements from nums1_copy and nums2
        # and add the smallest one into nums1.
        
        while p1 < m and p2 < n:
            
            if nums1_copy[p1] < nums2[p2]: 
                
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1

        # if there are still elements to add
        if p1 < m: 
            nums1[p1 + p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]

            


"""
VALID PALINDROME
"""

class Solution(object):
    
    def validPalindrome(self, s):
        
        for i in range(len(s)):
            
            t = s[:i] + s[i+1:]
            
            if t == t[::-1]: return True

        return s == s[::-1]
    
    
    
"""
VALID PALINDROME 2
"""   

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left, right = 0, len(s)-1

        while left < right:
            
            while left < right and not s[left].isalnum():
                left += 1
                
            while left < right and not s[right].isalnum():
                right -= 1

            if left < right and s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
    
    
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def rangeSumBST(self, rootNode, leftNode, rightNode):
        
        def dfs(node):
            
            if node:
                print(node)
                if leftNode <= node.val <= rightNode:
                    #add the value to our answer
                    self.answer += node.val
                    
                if leftNode < node.val:
                    #recurse into the left node
                    dfs(node.left)
                    
                if node.val < rightNode:
                    #recurse into the right node
                    dfs(node.right)

        self.answer = 0
        dfs(root)
        return self.answer
    
#test driver 
root = [10,5,15,3,7,null,18]
L = 7
R = 15


"""
REGULAR EXPRESSION MATCHING
"""
class Solution(object):
    def isMatch(self, text, pattern):
        memo = {}
        
        def dp(i, j):
            
            if (i, j) not in memo:
                
                if j == len(pattern):
                    
                    ans = i == len(text)
                else:
                    
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)


"""
SPLIT AN ARRAY
"""

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        l, output, j, k = len(nums), 0, 0, 0
        
        #accumulate() returns (e.g. if we have [1,2,3] = [1][1+2][1+2+3] or [1,3,6]
        nums = list(accumulate(nums))
        #loop through the length of the array - 2
        for i in range(l - 2):
            
            #left pointer
            while j <= i or (j < l - 1 and nums[j] < nums[i] * 2):
                print("j: ", j)
                j += 1
                
            #right pointer
            while k < j or (k < l - 1 and nums[k] - nums[i] <= nums[-1] - nums[k]):
                print("k: ", k)
                k += 1
            output = (output + k - j) % 1000000007
        return output
    