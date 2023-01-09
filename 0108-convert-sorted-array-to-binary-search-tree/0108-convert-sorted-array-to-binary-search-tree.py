# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        '''
          0   1 2 3 4
        [-10,-3,0,5,9]
              r l
        
        0 l=0 r=4 mid=2

        -3 l=0 r=1 mid=1 left=Node(10) right=None

        l=2 r=1

        -10  l=0 r=0 m=0
         0    1  2 3 4 5 6
        [-10,-3,-1,0,1,5,9]
                lr

        mid = r + l // 2

        leftSide = mid - 1

        mid is the root of each subtree

        right pointer of left subtree will be mid - 1
        left pointer of right subtree will be mid + 1
        '''


        def dfs(left, right):
            if left == right:
                return TreeNode(nums[left])
            if left > right:
                return None

            mid = (left + right) // 2

            root = TreeNode(nums[mid])  
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            return root
        
        return dfs(0, len(nums) - 1)
