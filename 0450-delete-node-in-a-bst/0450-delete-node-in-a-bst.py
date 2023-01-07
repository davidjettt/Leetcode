# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root, key):
        if not root:
            return False
        if key > root.val:
            return self.searchBST(root.right, key)
        elif key < root.val:
            return self.searchBST(root.left, key)
        else:
            return True

    def find_max_in_BST(self, root):
        curr = root
        while curr and curr.right:
            curr = curr.right
        return curr

    def removeNode(self, root, key):
        if key > root.val:
            root.right = self.removeNode(root.right, key)
        elif key < root.val:
            root.left = self.removeNode(root.left, key)
        else:
            # 0 children
            if not root.left and not root.right:
                return None
            # 1 child
            if not root.left or not root.right:
                if root.left and not root.right:
                    return root.left
                else:
                    return root.right
            # 2 children (valid replacements are max node val of left subtree or smallest node val of right subtree)
            if root.left and root.right:
                maxNode = self.find_max_in_BST(root.left)
                root.val = maxNode.val
                root.left = self.removeNode(root.left, maxNode.val)
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if self.searchBST(root, key):
            return self.removeNode(root, key)
        else:
            return root