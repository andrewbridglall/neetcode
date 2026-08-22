# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # tree to arr
        arr = []
        def preorder(root):
            # base csae
            # if root none
            if not root:
                arr.append('N')
                return
            # recursive case
            # process root
            arr.append(str(root.val))
            # run dfs left
            preorder(root.left)
            # run dfs right
            preorder(root.right)
        # return str 
        preorder(root)
        return "#".join(arr)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # set var i
        self.i = 0
        # given str
        arr = data.split("#")
        # arr to tree
        # iterate through arr and create nodes as we go -build tree
        def buildTree(i):
            # base case
            # if arr i eq N
            if arr[i] == 'N':
                return None
            # recursive case
            # create treenode with arr i - cast to int
            root = TreeNode(int(arr[i]))
            # set root.left - i +=1
            self.i+=1
            root.left = buildTree(self.i)
            # set root.right i+=1
            self.i+=1
            root.right = buildTree(self.i)
            # return root
            return root
        return buildTree(self.i)




