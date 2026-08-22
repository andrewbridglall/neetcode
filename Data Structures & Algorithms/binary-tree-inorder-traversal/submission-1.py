# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(node, traversal):
            if not node:
                return
            inorder(node.left, traversal)
            traversal.append(node.val)
            inorder(node.right, traversal)
        inorder(root, res)
        return res