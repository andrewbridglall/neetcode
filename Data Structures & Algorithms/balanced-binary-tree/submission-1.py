# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # make dfs
        def dfs(root):
            # base case
            if not root:
                return True, 0
            # recursive case
            # process children first then root
            lbalanced, lh = dfs(root.left)
            if not lbalanced:
                return False, -1
            rbalanced, rh = dfs(root.right)
            if not rbalanced:
                return False, -1
            if abs(lh-rh) > 1:
                return False, -1
            # post order traversal
            return True, max(lh, rh)+1
        # run dfs
        isbalanced, h = dfs(root)
        return isbalanced
