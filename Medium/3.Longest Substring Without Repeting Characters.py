# Given a string s, find the length of the longest substring without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.




class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        tmp_s = ''
        for j in s:
            if j in tmp_s:
                tmp_s = tmp_s[tmp_s.index(j)+1:] + j
            else:
                tmp_s += j
                tmp_len = len(tmp_s)
                max_len = tmp_len if tmp_len>max_len else max_len
                
        return max_len
