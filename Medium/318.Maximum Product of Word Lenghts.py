# Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.

 

# Example 1:

# Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# Explanation: The two words can be "abcw", "xtfn".
# Example 2:

# Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4
# Explanation: The two words can be "ab", "cd".
# Example 3:

# Input: words = ["a","aa","aaa","aaaa"]
# Output: 0
# Explanation: No such pair of words.




from typing import Optional, List
import math


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        dct = {}

        for i in words:
            val = 0
            for j in set(i):
                val |=  1<< (ord(j) - 97)

            dct[i] = val


        maax = 0

        for i in dct:
            for j in dct:
                if dct[i] & dct[j] == 0:
                    maax = max(maax, len(i)*len(j))

        return maax
                    
        



