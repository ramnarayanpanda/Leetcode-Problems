# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4







class Solution:
    def searchInsert(self, nums, target):
        import math

        def func(lo, hi):
            #print(lo,hi)
            if hi < lo:
                #print('1st if', lo)
                return hi + 1

            mid = math.ceil((hi + lo) / 2)

            if target > nums[mid]:
                #print('if')
                return func(mid + 1, hi)

            elif target < nums[mid]:
                #print('elif')
                return func(lo, mid - 1)

            else:
                #print('else')
                return mid

        #print(func(0, len(nums) - 1))
        return func(0, len(nums) - 1)







