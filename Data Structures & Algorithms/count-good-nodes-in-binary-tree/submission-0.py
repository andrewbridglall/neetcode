# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # preorder traversal and store curr max in stack
        # make dfs - count good nodes
        stack = []
        stack.append(float('-inf'))
        def dfs(root):
            # base case
            # if not root no good nodes to count
            if not root:
                return 0
            # recursive case
            # process root
            # compare root to max - if <= max not good, else if > - good
            count = 0
            newmax = False
            if stack[-1] <= root.val:
                count +=1
                # update max on stack
                newmax = True
                stack.append(root.val)
            
            # go to left child
            count += dfs(root.left)
            # go to right child
            count += dfs(root.right)
            # backtrack - pop from stack if root.val is max
            if newmax:
                stack.pop()
            return count
        # run dfs
        # return
        return dfs(root)