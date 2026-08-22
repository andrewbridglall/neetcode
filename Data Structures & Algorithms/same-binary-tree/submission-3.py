# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case
        # reach null
        if not p and not q:
            return True
        # one is null other is not
        if not p or not q:
            return False
        # recursive case

        # compare root vals
        
        # left
        l = self.isSameTree(p.left, q.left)
        # right
        r = self.isSameTree(p.right, q.right)
        
        # return default
        return p.val == q.val and l and r
