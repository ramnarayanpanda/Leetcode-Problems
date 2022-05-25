# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


from typing import Optional, List
import math


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        j = 0
        while j<min([len(i) for i in strs]):
            if len(set([i[j] for i in strs]))==1: j+=1
            else: break
                
        if j>0: return strs[0][:j]
        else: return ''