# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''

                1           
               /\
              2  3
              /\ /\
                 4
                /\
                6 

            1
            /
            2 
            /
            3 
        '''
        # Time O(n)
        # Space O(n)
        q = deque([root])
        res = []

        if not root:
            return res

        while q:
            most_right_node_at_level = q[-1].val
            res.append(most_right_node_at_level)
            for i in range(len(q)):
                node = q.popleft()
                # if i == 0:
                #     res.append(node.val)
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
        return res


        # res = []

        # def dfs(root):
        #     if not root:
        #         return
        #     res.append(root.val)
        #     if root.right:
        #         dfs(root.right)
        #     else:
        #         dfs(root.left)
        #     return
        # dfs(root)
        # return res
        
