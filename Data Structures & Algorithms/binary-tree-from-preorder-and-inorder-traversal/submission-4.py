# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {n:i for i,n in enumerate(inorder)}
        # base case
        if not preorder or not inorder:
            return None
        # recursive case
        # build root
        root = TreeNode(preorder[0])
        m = index[preorder[0]]
        # build root left
        root.left = self.buildTree(preorder[1:m+1], inorder[:m])
        # build root right
        root.right = self.buildTree(preorder[m+1:], inorder[m+1:])
        # return root
        return root