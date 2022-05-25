# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:

# Input: rowIndex = 0
# Output: [1]
# Example 3:

# Input: rowIndex = 1
# # Output: [1,1]






class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def func(n):
            if n==1: return [1]
            if n==2: return [1,1]

            lst = func(n-1)
            lst1 = [1]
            for i in range(1,n-1):
                lst1.append(lst[i-1] + lst[i])
            lst1.append(1)

            return lst1
        
        return func(rowIndex+1)
        
