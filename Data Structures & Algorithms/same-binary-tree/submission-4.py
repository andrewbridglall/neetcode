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
            if not p.val == q.val:
                return False
            # go left
            if not dfs(p.left, q.left):
                return False
            # go right
            if not dfs(p.right, q.right):
                return False
            # return
            return True
        return dfs(p,q)
