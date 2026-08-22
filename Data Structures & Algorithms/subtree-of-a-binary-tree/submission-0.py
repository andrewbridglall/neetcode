# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            
            if not isSameTree(p.left, q.left):
                return False
            if not isSameTree(p.right, q.right):
                return False
            return p.val == q.val

        def dfs(root):
            if not root:
                return False
            if isSameTree(root, subRoot):
                return True
            if dfs(root.left) or dfs(root.right):
                return True
            return False
        
        return dfs(root)