# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

 

# Example 1:

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
# Example 2:

# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:

# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.




from collections import defaultdict
from bisect import bisect_left


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        imap = defaultdict(list)
        for i, case in enumerate(text2):
            imap[case].append(-i)

        tail = []
        for case in text1[::-1]:
            for idx in imap[case]:
                j = bisect_left(tail, idx)
                if j == len(tail):
                    tail.append(idx)
                else:
                    tail[j] = idx

        return len(tail)