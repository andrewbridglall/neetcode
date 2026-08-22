# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightView = []
        if not root:
            return rightView

        queue = deque()
        queue.append(root)
        
        while queue:
            qL = len(queue)
            level = []
            for i in range(qL):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                level.append(curr.val)
            if level:
                rightView.append(level[-1])
        return rightView