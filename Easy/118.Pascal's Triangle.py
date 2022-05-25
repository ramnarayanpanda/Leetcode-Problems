# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]


from typing import Optional, List
import math




class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        glob_lst = []
        
        if numRows==1: return [[1]]
        if numRows==2: return [[1], [1,1]]
        
        
        def func(n):
            if n==1: return [1]
            if n==2: return [1,1]

            lst = func(n-1)
            lst1 = [1]
            for i in range(1,n-1):
                lst1.append(lst[i-1] + lst[i])
            lst1.append(1)
            glob_lst.append(lst1)

            return lst1
        
        func(numRows)
        
        return [[1], [1,1]] + glob_lst