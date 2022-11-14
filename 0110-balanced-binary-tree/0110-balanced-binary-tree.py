# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def treeHeight(self, root):
        if not root:
            return 0
        
        return 1 + max(self.treeHeight(root.left), self.treeHeight(root.right))
    
    
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left_side = self.treeHeight(root.left)
        right_side = self.treeHeight(root.right)
        
        if abs(left_side - right_side) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False
        