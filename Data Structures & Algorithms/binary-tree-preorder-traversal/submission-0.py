# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # iterative
        # declare and init stack, curr, res
        stack, curr, res = [], root, []
        # while curr or stack
        while curr or stack:
        # if curr - print root, save right subtree, traverse left subtree 
            if curr:
                res.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
        # else - reached end of left subtree, set curr = stack.pop()
            else:
                curr = stack.pop()
        return res