# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        # make currSum variable
        # add node.val to currSum variable at each traversal
        # make a check before adding the num to currSum
            # if currSum > targetSum
                # go to the other path
            # if currSum < targetSum
                # keep traversing
                
        # return false once we have touched all nodes
        
        def dfs(node, curr_sum):
            if not node:
                return False
            
            curr_sum += node.val
            if not node.left and not node.right:
                return curr_sum == targetSum
            
            return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)
        
        return dfs(root, 0)
        
        
        