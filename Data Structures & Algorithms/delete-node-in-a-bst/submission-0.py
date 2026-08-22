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
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            #key == root.val - arrived at node to remove
            # 0 children
            # 1 child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minVal = self.findMin(root.right)
                root.val = minVal
                root.right = self.deleteNode(root.right, minVal)
        return root
            # 2 children
    
    def findMin(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr.val