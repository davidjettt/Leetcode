# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        q = deque()
        q.append(root)
        root.level = 0
        
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            res.append(level)
        return res
        
#         while len(q) > 0:
#             current = q.pop(0)
            
#             if len(res) > 0 and res[current.level]: 
#                 res[current.level].append(current.val)
#             else:
#                 res.append([current.val])
                

#             if current.left:
#                 current.left.level = current.level + 1
#                 q.append(current.left)
#             if current.right:
#                 current.right.level = current.level + 1
#                 q.append(current.right)

#         return res
        