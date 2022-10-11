# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        if not root:
            return []
        
        q = deque()
        q.append(root)
        res = []
        
        while len(q) > 0:
            level = []
            
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # Time O(n) 
            level_avg = sum(level) / len(level)
            res.append(level_avg)
        
        return res
        