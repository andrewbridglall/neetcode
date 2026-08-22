# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # bf
        if not root:
            return -1
        # init vars
        arr = []
        # run inorder dfs on bst
        def dfs(root):
            if not root:
                return
            # root left
            dfs(root.left)
            # process root
            arr.append(root.val)
            # root right
            dfs(root.right)
        
        # call dfs
        dfs(root)
        # return index k-1
        return arr[k-1]