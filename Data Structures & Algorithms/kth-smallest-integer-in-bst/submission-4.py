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
        # arr = []
        res = -1
        count = 0
        # run inorder dfs on bst
        def dfs(root):
            nonlocal count
            nonlocal res
            if not root or count >= k:
                return
            # root left
            dfs(root.left)
            # process root
            count +=1
            print(root.val)
            if count == k:
                res = root.val
                return
            # root right
            dfs(root.right)
        
        # call dfs
        dfs(root)
        # return index k-1
        return res