# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.



from typing import Optional, List
import math


class Solution:
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        n1, n2 = len(num1), len(num2)
        nn1, nn2 = 0, 0
        ret_lst = []
        
        while (nn1<n1) and (nn2<n2):
            if num1[nn1]<=num2[nn2]: 
                ret_lst.append(num1[nn1])
                nn1+=1
            elif num1[nn1]>num2[nn2]:
                ret_lst.append(num2[nn2])
                nn2+=1
        
        while nn1<n1:
            ret_lst.append(num1[nn1])
            nn1+=1
            
        while nn2<n2:
            ret_lst.append(num2[nn2])
            nn2+=1
            
        n = (n1+n2)//2
        if (n1+n2)%2==0:
            return (ret_lst[n-1] + ret_lst[n]) / 2
        return ret_lst[n]