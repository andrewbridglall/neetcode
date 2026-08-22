# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # init vars
        q = collections.deque()
        res = []
        if root:
            q.append(root)
        # run bfs
        while q:
            level = []
            for _ in range(len(q)):
                # curr = popleft
                curr = q.popleft()
                # add to level arr
                level.append(curr.val)
                # add left and right if exist
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            # append level to res
            res.append(level)
        # return res
        return res