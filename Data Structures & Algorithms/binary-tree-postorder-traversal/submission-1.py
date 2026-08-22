# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative
        # stack, visit
        stack, visit, res = [root], [False], []
        # while stack
        while stack:
            curr, visited = stack.pop(), visit.pop()
        # if visit - add to res
            if curr:
                if visited:
                    res.append(curr.val)
        # if not visited - add root, T, add root.right F, add root.left F
                else:
                    stack.append(curr)
                    visit.append(True)
                    stack.append(curr.right)
                    visit.append(False)
                    stack.append(curr.left)
                    visit.append(False)
        # return res
        return res