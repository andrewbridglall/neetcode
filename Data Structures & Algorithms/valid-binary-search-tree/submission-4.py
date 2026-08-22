# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # bst recursive soln with valid range stored
        def dfs(root, l, r):
            # base case
            # if root is none - valid bst return true
            if not root:
                return True
            # recursive case
            # go left - new range is l to root.val
            if not dfs(root.left, l, root.val):
                return False
            # go right - new range is root.val to r
            if not dfs(root.right, root.val, r):
                return False
            # check root.val in (l,r)
            # return
            return l < root.val < r
        return dfs(root, float('-inf'), float('inf'))
