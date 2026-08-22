class SegmentNode:
    def __init__(self, total, l, r):
        self.total = total
        self.l = l
        self.r = r
        self.left = None
        self.right = None

class SegmentTree:
    
    def __init__(self, nums: List[int]):
        # init "segment tree node" structure
        # build segment tree
        self.root = SegmentTree.build(nums, 0, len(nums)-1)
    
    @staticmethod
    def build(nums, l, r):
        # base case
        if l == r:
            return SegmentNode(nums[l], l, r)
        # recursive case
        root = SegmentNode(0, l, r)
        m = (l+r)//2
        root.left = SegmentTree.build(nums, l, m)
        root.right = SegmentTree.build(nums, m+1, r)
        root.total = root.left.total+root.right.total
        return root

    def update(self, index: int, val: int) -> None:
        return self.updateHelper(self.root, index, val)
    
    def updateHelper(self, node, index: int, val: int) -> None:
        # base case
        if node.l == node.r:
            node.total = val
            return
        # recursive case
        m = (node.l + node.r)//2
        if index < m+1:
            self.updateHelper(node.left, index, val)
        else:
            self.updateHelper(node.right, index, val)
        # get new sum
        node.total = node.left.total + node.right.total
    
    def query(self, L: int, R: int) -> int:
        return self.queryHelper(self.root, L, R)
    
    def queryHelper(self, node, L: int, R: int) -> int:
        # base case
        if node.l == L and node.r == R:
            return node.total
        # recursive case
        m = (node.l + node.r)//2
        if R < m+1:
            return self.queryHelper(node.left, L, R)
        elif L > m:
            return self.queryHelper(node.right, L,R)
        else:
            return self.queryHelper(node.left, L, m) + \
            self.queryHelper(node.right, m+1, R)

