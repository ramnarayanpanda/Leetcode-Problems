# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)


# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"





class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows, direction, i = [[] for _ in range(numRows)], 1, 0
        for ch in s:
            rows[i].append(ch)
            i = min(numRows - 1, max(0, i + direction))
            if i == 0 or i == numRows - 1: direction *= -1
        return ''.join(''.join(row) for row in rows)