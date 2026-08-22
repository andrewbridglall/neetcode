# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # base case - root is none - may already be handled
        if not root:
            return True
        # recursive  case
        # process root
        
        # go left
        
        # go right
        
        return (self.dfsLeft(root.left, root.val) and 
                self.dfsRight(root.right, root.val) and 
                 self.isValidBST(root.left) and self.isValidBST(root.right))
        
    
    # dfs - compare every node val to current root val
    def dfsLeft(self, root, target):
        if not root:
            return True
        return (root.val < target and  
                self.dfsLeft(root.left, target) and 
                self.dfsLeft(root.right, target))
    
    # dfs - compare every node val to current root val
    def dfsRight(self, root, target):
        if not root:
            return True
        return (root.val > target and  
                self.dfsRight(root.left, target) and 
                self.dfsRight(root.right, target))
    