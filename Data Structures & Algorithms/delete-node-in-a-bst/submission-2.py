# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        # search for node to remove
        def getMin(node):
            curr = node
            while curr and curr.left:
                curr = curr.left
            return curr
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
                
            # remove - cases 0-1 child, 2 children
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minVal = getMin(root.right).val
                root.val = minVal
                root.right = self.deleteNode(root.right, minVal)
        return root
        # 2 children - declare func to find min of right subtree


