# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursive func to calc max height at given node
        def dfs(root):
            # base case
            # if root is none - height or max depth of null tree is 0
            if not root:
                return 0
            # recursive case
            # otherwise root is non null
            # max depth is 1 + max height left subtree and right subtree
            return 1 + max(dfs(root.left), dfs(root.right))
        # call func on root
        # return result
        return dfs(root)