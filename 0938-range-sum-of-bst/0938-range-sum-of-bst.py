# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # need to find the sum of all nodes with values between low and high inclusive
        
        res = 0
        stack = [ root ]   # stack = FILO / LOFI
        
        while len(stack) > 0:
            current = stack.pop()
            
            if low <= current.val <= high:
                res += current.val
                
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
                
        return res
        
        