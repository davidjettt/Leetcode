# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''

        do dfs on root
        continue until root.val is equal to subRoot.val
            if find a match, then do dfs on both roots check for matching structure/node values
                if at any point there isn't a match return false (continue with first dfs in case there are more matches)
                but if finish dfs on subRoot then immediately return True b/c found the subtree

        '''
        # Time O(n * m) where n is size of first tree and m is size of second tree
        # Space O(n) where n is size of the first tree
        
        if not root:
            return False
        # if find suspected match run dfs on both roots to check for matching descendants
        if root.val == subRoot.val:
            match = self.sameTree(root, subRoot)
            if match:
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    
    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val != subRoot.val:
            return False
        
        return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        

        