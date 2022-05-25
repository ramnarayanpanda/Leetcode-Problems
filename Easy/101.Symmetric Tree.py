# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Example 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false



from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        
        def func(p, q):
        
            if not p and not q:
                return True

            elif not (p and q):
                return False

            elif p.val!=q.val:
                return False

            return func(p.left, q.right) and func(p.right, q.left)
        
        return func(root.left, root.right)
        
        
        