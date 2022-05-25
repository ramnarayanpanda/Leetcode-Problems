# Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

# A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

 

# Example 1:

# Input: str1 = "abac", str2 = "cab"
# Output: "cabac"
# Explanation: 
# str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
# str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
# The answer provided is the shortest such string that satisfies these properties.
# Example 2:

# Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
# Output: "aaaaaaaa"





class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        def LCS(t):
            for i in range(1, len(s1) + 1):
                for j in range(1, len(s2) + 1):
                    # print(i,j)
                    if s1[i - 1] == s2[j - 1]:
                        t[i][j] = 1 + t[i - 1][j - 1]
                    else:
                        t[i][j] = max(t[i - 1][j], t[i][j - 1])
            return t[len(s1)][len(s2)]

        t = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
        LCS(t)
        s = ''
        i, j = len(s1), len(s2)
        while (i > 0) and (j > 0):
            if s1[i - 1] == s2[j - 1]:
                s += s1[i - 1]
                i -= 1
                j -= 1
            else:
                if t[i][j - 1] > t[i - 1][j]:
                    j -= 1
                else:
                    i -= 1
        lcs = s[::-1]

        # i -> to iterate over lcs
        # j -> to iterate over s1
        # k -> to iterate over s2
        i, j, k = 0, 0, 0
        scs = ''
        #print(lcs)

        while i < len(lcs) and j < len(s1) and k < len(s2):
            while s1[j] != lcs[i]:
                scs += s1[j]
                j += 1
            while s2[k] != lcs[i]:
                scs += s2[k]
                k += 1
            scs += lcs[i]
            i, j, k = i + 1, j + 1, k + 1
            # print(i, j, k, scs)

        # print(scs)
        while j < len(s1):
            scs += s1[j]
            j += 1
        while k < len(s2):
            scs += s2[k]
            k += 1

        # cabefhcgb
        return scs




