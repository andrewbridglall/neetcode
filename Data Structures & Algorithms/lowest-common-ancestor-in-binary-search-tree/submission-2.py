# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # search for nodes p and q and add to arr
        def getAncestors(curr, target):
            arr = []
            while curr:
                # store curr
                arr.append(curr)
                if target < curr.val:
                    curr = curr.left
                elif target > curr.val:
                    curr = curr.right
                else:
                    break
            return arr if curr else []
        
        ancP, ancQ = getAncestors(root, p.val), getAncestors(root, q.val)
        
        # iterate through arr to get latest common node aka lca
        res = None
        i = 0
        while i != min(len(ancP), len(ancQ)):
            if ancP[i] == ancQ[i]:
                res = ancP[i]
                i+=1
            else:
                break
        # return node
        return res