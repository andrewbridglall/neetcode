# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.ptr = 0
        self.traversal = []
        self.traversal.append(-1)
        
        stack, curr = [], root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                self.traversal.append(curr.val)
                curr = curr.right
        print(self.traversal)

    def next(self) -> int:
        self.ptr +=1
        return self.traversal[self.ptr]

    def hasNext(self) -> bool:
        return self.ptr+1 < len(self.traversal)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()