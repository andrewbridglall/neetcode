# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def inorder(self, root, arr):
        if not root:
            return
        self.inorder(root.left, arr)
        arr.append(root.val)
        self.inorder(root.right, arr)
    
    def preorder(self, root, arr):
        if not root:
            return
        arr.append(root.val)
        self.preorder(root.left, arr)
        self.preorder(root.right, arr)

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # build inorder preorder traversal
        inorder, preorder = [], []
        self.inorder(root, inorder)
        self.preorder(root, preorder)
        # encode inorder and preoder as string
        inorderStr, preorderStr = '', ''
        for n in inorder:
            inorderStr += str(n)+'#'
        for n in preorder:
            preorderStr += str(n)+'#'
        # concat
        res = inorderStr + '?' + preorderStr
        # return str
        return res
    
    def buildTree(self, inorder, preorder):
        index = {n:i for i,n in enumerate(inorder)}
        # base case
        if not inorder or not preorder:
            return None
        # recursive case
        root = TreeNode(preorder[0])
        m = index[preorder[0]]
        root.left = self.buildTree(inorder[:m], preorder[1:m+1])
        root.right = self.buildTree(inorder[m+1:], preorder[m+1:])
        return root

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # decode into inorder and preorder
        inorderStr, preorderStr = data.split('?')
        inorder = [int(s) for s in inorderStr.split('#')[:-1]]
        preorder = [int(s) for s in preorderStr.split('#')[:-1]]
        # build tree from inorder and preorder
        root = self.buildTree(inorder, preorder)
        # return root of tree
        return root
