# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false





class Solution:
    def isValid(self, s: str) -> bool:
        lst = []

        for i in s:
            if (len(lst) == 0) or not ((i == ')' and lst[-1] == '(') or (i == '}' and lst[-1] == '{') or (i == ']' and lst[-1] == '[')):
                lst.append(i)
                continue
            lst.pop()
        if len(lst) == 0:
            return True
        else:
            return False