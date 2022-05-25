# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

# You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

 

# Example 1:

# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.
# Example 2:

# Input: nums = [-1,0]
# Output: [-1,0]
# Example 3:

# Input: nums = [0,1]
# Output: [1,0]







class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        val = 0
        for i in nums:
            val ^= i
            
        xr_mask = (val & (val-1)) ^ val
            
        xr_a, xr_b = 0, 0
        for i in nums:
            if xr_mask&i ==0:
                xr_a ^= i
                
            else:
                xr_b ^= i
                
        return [xr_a, xr_b]








