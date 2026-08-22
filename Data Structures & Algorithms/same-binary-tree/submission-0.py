# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case
        # if p q both none ret Tr
        if not p and not q:
            return True
        # if p or q none or p q neq ret False
        if not p or not q:
            return False
        # recursive case
        # if not p q val
        if p.val != q.val:
            return False
        # if not  p left q left
        if not self.isSameTree(p.left, q.left):
            return False
        # if not p right q right
        if not self.isSameTree(p.right, q.right):
            return False
        # default true
        return True