# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 08:54:06 2021

@author: SethHarden
"""

class Solution:
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
                
                # max() returns the greater number
                # index is assigned either the index store for that letter or the current one
                index = max(value_index[letters[letter]], index)

                
            answer = max(answer, letter - index + 1)
            
            value_index[letters[letter]] = letter + 1

        return answer
    
if __name__ == "__main__":
    s = "eabcabcbbne"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))
