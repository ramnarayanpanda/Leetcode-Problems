# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]




from typing import Optional, List
import math



class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        set1 = set()
        set1.add(tuple())
        n = len(nums)
        
        for i in range(1, 2**n):
            lst1 = []
            for j in range(n):
                if (i>>j) & 1 == 1:
                    lst1.append(nums[j])
                    
            set1.add(tuple(sorted(lst1)))
            
        return set1