# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        if root.val == val:
            return root
        
        return self.searchBST(root.left, val)  or self.searchBST(root.right, val) 
        # self.searchBST(root.right, val)
        
#         stack = [ root ]
#         while len(stack) > 0:
#             curr = stack.pop()
            
#             if curr.val == val:
#                 return curr
#             else:
#                 if curr.left:
#                     stack.append(curr.left)
#                 if curr.right:
#                     stack.append(curr.right)

#         return None
    
    