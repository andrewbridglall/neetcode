# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {n:i for i,n in enumerate(inorder)}

        self.preIndex = 0

        def dfs(l,r):
            if l > r:
                return None
            
            rootval = preorder[self.preIndex]
            mid = index[rootval]
            self.preIndex +=1
            
            root = TreeNode(rootval)
            root.left = dfs(l, mid-1)
            root.right = dfs(mid+1, r)
            return root
        return dfs(0,len(inorder)-1)