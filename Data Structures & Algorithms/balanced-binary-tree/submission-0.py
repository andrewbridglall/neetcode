# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # calc height and compare height

        # make dfs
        def dfs(root):
            # base case
            if not root:
                return True, 0
            # recursive case
            lb, lh = dfs(root.left)
            rb, rh = dfs(root.right)
            if not lb or not rb:
                return False, -1
            if abs(lh-rh) > 1:
                return False, -1
            return True, 1 + max(lh, rh)
            
        # run dfs
        rootBal, _ = dfs(root)
        # return
        return rootBal