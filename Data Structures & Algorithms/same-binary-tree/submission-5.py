# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # run dfs
        def dfs(p,q):
        # base case
            if not p and not q:
                return True
            if not p or not q:
                return False
        # recursive case
            # process root
            root = p.val == q.val
            left = dfs(p.left, q.left)
            right = dfs(p.right, q.right)
            return root and left and right
        return dfs(p,q)
