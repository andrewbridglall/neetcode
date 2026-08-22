# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs
        # init vars
        q = collections.deque()
        res = []
        # init ds
        if root:
            q.append(root)
        # run bfs
        while q:
            # init levels
            level = []
            for _ in range(len(q)):
                # curr = popleft
                curr = q.popleft()
                level.append(curr.val)
                # add curr to level
                # add curr left curr right if exist
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            # take right most elt in level and append to res
            res.append(level[-1])
        # return res
        return res