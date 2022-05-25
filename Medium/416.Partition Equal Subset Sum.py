# Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

 

# Example 1:

# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:

# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.


from typing import List




class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def func(n, s, st):
            #print(n, s, st)
            if s == 0: return 1
            if n >= N: return 0
            if t[n+1][s]!=-1: return t[n+1][s]

            if s - lst[n] >= 0:
                t[n + 1][s] = func(n + 1, s - lst[n], 1) or func(n + 1, s, 2)
                return t[n + 1][s]
            else:
                t[n + 1][s] = func(n + 1, s, 2)
                return t[n + 1][s]


        if sum(nums)%2!=0: return 0
        else:
            lst = sorted(nums, reverse=True)
            # print(lst)
            S = int(sum(nums)/2)
            N = len(nums)
            t = [[-1 for i in range(S + 1)] for j in range(N + 1)]
            t[0][0] = True
            #print(S,N)
            for i in range(1, S + 1):
                t[0][i] = False
            for i in range(1, N + 1):
                t[i][0] = True

            return func(0, S, 1)
        