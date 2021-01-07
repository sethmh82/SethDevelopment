# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 08:32:16 2021

@author: SethHarden
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s) #get the length
        ans = 0 #initialize ans
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        #loop j n times
        for j in range(n): 
            # loop through characters of the string and see if its in our dictionary
            if s[j] in mp: 
                #if it is assign i 
                print(j)
                i = max(mp[s[j]], i)
            print(i)
            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans
    
if __name__ == "__main__":
    s = "abcabcbb"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))