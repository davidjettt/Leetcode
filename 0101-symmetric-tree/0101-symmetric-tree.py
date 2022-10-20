# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        
#              1
#             / \
#            2   2
#           / \ / \
#             3 3



        if not root:
            return True
        
        
        return self.isMirror(root.left, root.right)
    
    
    
    def isMirror(self, leftRoot, rightRoot):
        if not leftRoot and not rightRoot:
            return True
        if not leftRoot or not rightRoot:
            return False
        
        
        if leftRoot.val == rightRoot.val:
            firstPair = self.isMirror(leftRoot.left, rightRoot.right)
            secondPair = self.isMirror(leftRoot.right, rightRoot.left)
            
            return firstPair and secondPair
        
        