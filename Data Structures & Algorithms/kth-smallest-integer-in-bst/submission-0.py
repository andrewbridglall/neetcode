# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal and create arr
        arr = []
        self.inorder(root, arr)
        return arr[k-1]
        # return arr[k-1]
    
    def inorder(self, root, array):
        if not root:
            return
        self.inorder(root.left, array)
        array.append(root.val)
        self.inorder(root.right, array)