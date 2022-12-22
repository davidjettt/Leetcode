# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import trunc
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        '''

        complete binary tree = nodes are filled top to down, left to right

        algos logn: binary search, heapsort, searching BST

        num of nodes at each level grows exponentially -> 2^h - 1

        LEVEL   # NODES
        1       1
        2       2
        3       4
        4       8   
        5       16
        6       32

        height of binary tree is logn
        do dfs to figure out height of tree
        return back that number

        2^2 = 4
        2^1 = 2
              1

        '''
        if not root:
            return 0

        def left_height(node):
            if not node:
                return 0
            return 1 + left_height(node.left)
        def right_height(node):
            if not node:
                return 0
            return 1 + right_height(node.right)

        left, right = left_height(root), right_height(root)

        if left > right:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        else:
            return (2 ** left) - 1


        