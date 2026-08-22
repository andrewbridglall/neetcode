# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # run dfs where we calc max if we branch and don't branch
        def dfs(root):
            # base case
            # if root none
            if not root:
                return float('-inf'), float('-inf')
            # recursive case
            left_nob, left_b = dfs(root.left)
            right_nob, right_b = dfs(root.right)
            no_branch = max(root.val, root.val+left_nob, root.val+right_nob)
            branch = max(root.val+left_nob+right_nob, left_nob, left_b, right_nob, right_b)
            # return
            return no_branch, branch
        
        return max(dfs(root))