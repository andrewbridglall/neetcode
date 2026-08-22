# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # search for p
        # append path to p
        # search for q
        # append path to q
        def search(root, target, path):
            # base case
            if not root:
                return []
            # recursive case
            path.append(root)
            if target < root.val:
                return search(root.left, target, path)
            if target > root.val:
                return search(root.right, target, path)
            return path
        
        pathP = search(root, p.val, [])
        pathQ = search(root, q.val, [])

        # iaterate through paths and record last common val
        i = 0
        res = None
        while i < min(len(pathP), len(pathQ)):
            if pathP[i] == pathQ[i]:
                res = pathP[i]
            else:
                break
            i+=1
        # return
        return res
