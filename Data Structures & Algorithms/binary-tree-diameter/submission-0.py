# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # make dfs to get longest path from given node
        # diameter = lh + rh
        d = 0
        # return max lh rh +1
        # keep track of max diamter
        def dfs(root):
            # base case
            if not root:
                return 0 # height of null node is 0
            # recursive case
            lh = dfs(root.left)
            rh = dfs(root.right)
            nonlocal d
            d = max(d, lh+rh)
            return max(lh, rh) +1
        # run dfs
        dfs(root)
        # return res
        return d