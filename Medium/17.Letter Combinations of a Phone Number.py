# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
# Return the answer in any order.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]





ph_dct = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno',
          '7':'pqrs', '8':'tuv', '9':'wxyz'}

from typing import List

class Solution:
    def rec_func(self, lst1, lst2):
        lst = []

        if len(lst1) == 0 and len(lst2) == 0: return []
        if len(lst2)==0: return lst1

        for i in lst1:
            s = i
            for j in lst2:
                lst.append(s+j)
        return lst

    def letterCombinations(self, digits: str) -> List[str]:
        int_lst = []
        for i in digits[::-1]:
            int_lst = self.rec_func(ph_dct[i] ,int_lst)
        return int_lst

print(Solution().letterCombinations('23'))