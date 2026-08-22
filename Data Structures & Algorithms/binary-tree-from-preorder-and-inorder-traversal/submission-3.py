# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {n:i for i,n in enumerate(inorder)}
        i = 0
        def dfs(l,r):
            # base case
            if l>r:
                return None    
            # recursive case
            nonlocal i
            root_val = preorder[i]
            i+=1
            root = TreeNode(root_val)
            m = index[root_val]
            root.left = dfs(l, m-1)
            root.right = dfs(m+1, r)
            return root
        
        return dfs(0, len(preorder)-1)
