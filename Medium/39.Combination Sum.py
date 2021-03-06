# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []


from typing import Optional, List
import math



class Solution:
    def my_init(self, candidates):
        self.candidates = sorted(candidates)
        self.output = []
        self.length = len(self.candidates)

    def backtrack(self, target, cur_lst, pos):
        if target==0:
            self.output.append(cur_lst)
            return True

        for i in range(pos,self.length):
            pop_ele = self.candidates[i]
            if pop_ele > target:
                break
            self.backtrack(target-pop_ele, cur_lst+[pop_ele], i)
        return False


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.my_init(candidates)
        self.backtrack(target, [], 0)
        return self.output






