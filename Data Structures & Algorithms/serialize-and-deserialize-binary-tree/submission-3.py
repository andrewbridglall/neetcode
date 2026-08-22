# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # implement preorder with nones
        preorder = []
        def dfs(root):
            if not root:
                preorder.append('N')
                return
            preorder.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)

        # encode preorder traversal to str
        # check edge cases if preorder empty
        res = '#'.join(preorder)
        # ret str
        return res

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # decode str to preorder
        preorder = data.split('#')
        # vals still str

        # build tree from preorder
        # recursively
        self.preIdx = 0
        def buildTree():
            # base case
            # if val == none, return None
            if preorder[self.preIdx] == 'N':
                self.preIdx +=1
                return None
            # recursive case
            # build root
            root = TreeNode(int(preorder[self.preIdx]))
            self.preIdx +=1
            # root.left buildTree
            root.left = buildTree()
            # root.right buildTree
            root.right = buildTree()
            # return root
            return root
        return buildTree()