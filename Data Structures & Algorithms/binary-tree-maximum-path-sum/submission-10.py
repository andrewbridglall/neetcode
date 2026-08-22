# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # make dfs
        def dfs(root):
            # base case
            # if root none ret 0, 0 - no max
            if not root:
                return float('-inf'),float('-inf')
            # recursive case
            # build incl excl max
            inclLeft, exclLeft = dfs(root.left)
            inclRight, exclRight = dfs(root.right)
            incl = max(root.val, root.val+inclLeft, root.val+inclRight)
            excl = max(incl, exclLeft, exclRight, root.val + inclLeft + inclRight)
            return incl, excl
            # return tuple
        # run dfs
        # return max dfs
        return max(dfs(root))