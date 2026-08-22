# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # init vars
        self.d = 0
        # make dfs
        def dfs(root):
            # base case
            if not root:
                return 0 # height is 0
            # recursive case
            lheight = 1 + dfs(root.left)
            rheight = 1 + dfs(root.right)
            self.d = max(self.d, lheight-1 + rheight-1)
            return max(lheight, rheight)
        # run dfs
        dfs(root)
        # return diameter
        return self.d