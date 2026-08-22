class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        self.root = self.insertHelper(self.root, key, val)
    
    def insertHelper(self, node, key, val):
        if not node:
            return TreeNode(key, val)
        
        if key > node.key:
            node.right = self.insertHelper(node.right, key, val)
        elif key < node.key:
            node.left = self.insertHelper(node.left, key, val)
        else:
            node.val = val
        return node

    def get(self, key: int) -> int:
        return self.searchHelper(self.root, key)
    
    def searchHelper(self, node, key):
        if not node:
            return -1
        if key > node.key:
            return self.searchHelper(node.right, key)
        elif key < node.key:
            return self.searchHelper(node.left, key)
        return node.val

    def getMin(self) -> int:
        if not self.root:
            return -1
        return self.findMin(self.root).val


    def getMax(self) -> int:
        if not self.root:
            return -1
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.val

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)
    
    def removeHelper(self, node, key):
        if not node:
            return None
        
        if key > node.key:
            node.right = self.removeHelper(node.right, key)
        elif key < node.key:
            node.left = self.removeHelper(node.left, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                minNode = self.findMin(node.right)
                node.key = minNode.key
                node.val = minNode.val
                node.right = self.removeHelper(node.right, minNode.key)
        return node
    
    def findMin(self, node):
        curr = node
        while curr and curr.left:
            curr = curr.left
        return curr


    def getInorderKeys(self) -> List[int]:
        res = []
        self.inorderHelper(self.root, res)
        return res
    
    def inorderHelper(self, node, traversal):
        if not node:
            return
        self.inorderHelper(node.left, traversal)
        traversal.append(node.key)
        self.inorderHelper(node.right, traversal)
