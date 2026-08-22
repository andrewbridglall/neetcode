# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # recursive soln
        print(root.val)
        # base case
        if root.val == p.val:
            return p
        if root.val == q.val:
            return q
        if min(p.val, q.val) < root.val < max(p.val, q.val):
            return root
        # recusrive case
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p,q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p,q)