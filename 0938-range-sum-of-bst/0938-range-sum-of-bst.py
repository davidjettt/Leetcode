# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # need to find the sum of all nodes with values between low and high inclusive
        
        if not root:
            return 0
        res = 0
        if low <= root.val <= high:
            res += root.val
        if root.val > low:
            res += self.rangeSumBST(root.left, low, high)
        if root.val < high:
            res += self.rangeSumBST(root.right, low, high)
        return res
#         sum_vals = 0
#         left = self.rangeSumBST(root.left, low, high)
#         right = self.rangeSumBST(root.right, low, high)
        
#         if low <= left <= high:
#             sum_vals += left
#         if low <= right <= high:
#             sum_vals += right
#         if low <= root.val <= high:
#             sum_vals += root.val
        
#         return sum_vals
        
        
#         res = 0
#         stack = [ root ]   # stack = FILO / LOFI
        
#         while len(stack) > 0:
#             current = stack.pop()
            
#             if low <= current.val <= high:
#                 res += current.val
                
#             if current.left:
#                 stack.append(current.left)
#             if current.right:
#                 stack.append(current.right)
                
#         return res
    
        # Time O(n)  # iterating through n nodes
        # Space O(n)  # using stack like data structure
        
        