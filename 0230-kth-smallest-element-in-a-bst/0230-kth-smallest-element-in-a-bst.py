# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        given root of a BST

        we want to return kth smallest value in BST

        traversing BTS -> dfs / bfs
        
        in order traversal prints vals in ascending order for BST

        '''
        
        nums = []
        def inOrder(root):
            if not root:
                return
            
            inOrder(root.left)
            nums.append(root.val)
            inOrder(root.right)
            return
        
        inOrder(root)
        
        return nums[k-1]