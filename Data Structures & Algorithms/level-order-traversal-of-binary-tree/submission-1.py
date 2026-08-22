# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # check root not null
        if not root:
            return []
        # declare queue
        # add root to queue
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            qlen = len(queue)
            currlevel = []
            for i in range(qlen):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                currlevel.append(curr.val) 
            res.append(currlevel)
        return res
        # while queue nonempty
        # - for elt in queue
        # -- curr = queue.popleft
        # -- if curr has neighbors append to queue
        # done with current level so incrememtn level