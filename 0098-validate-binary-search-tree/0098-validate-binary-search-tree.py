# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
            6
           / \
          /   \
         3      9
        /\     / \
       /  \   /   \
      1    4  7   11
     / \
    /   \
   0     2
  / 
 /
10

        base case:
            if root is null, then true

        if root.left < root then make recursive call on root.left
            if check is false then return false immediately

        if root.right > root then make recursive call on root.right
            same for right side

        '''
        # Time O(n)
        # Space O(n)
        def validate(node, left, right):
            if not node:
                return True
            if not (node.val > left and node.val < right):
                return False
            return (validate(node.left, left, node.val) and
                    validate(node.right, node.val, right))
        
        return validate(root, float('-inf'), float('inf'))
        

