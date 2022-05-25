# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3




class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            x = nums[i] % len(nums)
            nums[x] += len(nums)
            
            
        maax = 0
        idx = 0
        
        for i in range(len(nums)):
            
            if maax<nums[i]:
                idx = i
                maax = nums[i]
                
            nums[i] = nums[i] % len(nums)
            
        return idx