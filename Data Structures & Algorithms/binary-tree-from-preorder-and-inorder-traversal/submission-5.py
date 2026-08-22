# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # recursive
        # init vars
        # make dfs
        def dfs(preorder, inorder):
            index = {n:i for i,n in enumerate(inorder)}
            # base case
            # empty arr - return None
            if not preorder or not inorder:
                return None
            # recrusive case
            # build root
            root = TreeNode(preorder[0])
            m = index[preorder[0]]
            # root left
            root.left = dfs(preorder[1:m+1], inorder[:m])
            # inorder 0..m-1, preorder 1...m
            # root right
            root.right = dfs(preorder[m+1:], inorder[m+1:])
            # inorder m+1 ... end, preorder m+1 .. end
            # return root
            return root

        # run dfs
        # return root
        return dfs(preorder, inorder)