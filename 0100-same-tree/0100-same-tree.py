# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
        
    
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         # Time O(n + m)
#         # Space O(n + m)
#         x = []
#         y = []
        
#         def dfs(node, check):
#             if not node:
#                 if check == 'p':
#                     x.append(None)
#                     return
#                 else:
#                     y.append(None)
#                     return
#             if check == 'p':
#                 x.append(node.val) 
#             else:
#                 y.append(node.val)
                
#             dfs(node.left, check)
#             dfs(node.right, check)
                
#         dfs(p, 'p')
#         dfs(q, 'q')
#         return x == y
        
        