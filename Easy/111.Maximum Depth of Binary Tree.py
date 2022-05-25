# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 2
# Example 2:

# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5



from typing import Optional



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    
    # Approach: Min depth is the no of nodes from head to the farest leaf node
    
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def func(node):
            if not node: return 0
            
            left_depth = func(node.left)
            right_depth = func(node.right)
            
            if not left_depth or not right_depth:
                return 1 + max(left_depth, right_depth)
            
            return 1 + min(left_depth, right_depth)
        
        return func(root)






