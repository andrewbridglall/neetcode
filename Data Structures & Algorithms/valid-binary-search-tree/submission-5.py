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
            left = dfs(root.left, l, root.val)
            # go right - new range is root.val to r
            right = dfs(root.right, root.val, r)
            # check root.val in (l,r)
            # return
            return left and right and l < root.val < r
        return dfs(root, float('-inf'), float('inf'))
