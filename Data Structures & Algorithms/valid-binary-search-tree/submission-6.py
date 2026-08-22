# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # run dfs
        # check if root val in valid range
        def dfs(root, l, r):
            # base case
            # if not node ret true
            if not root:
                return True
            # recursive case
            # process root - check in range
            if not l < root.val < r:
                return False
            # left subtree - range l, root.val
            if not dfs(root.left, l, root.val):
                return False
            # right subtree - range root.val, r
            if not dfs(root.right, root.val, r):
                return False
            # if all conditions true return true else false
            return True
        # run dfs
        return dfs(root, float('-inf'), float('inf'))