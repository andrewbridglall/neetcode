# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # run bfs
        q = collections.deque()
        res = []
        q.append(root)

        while q:
            for _ in range(len(q)):
                # pop
                # append to res
                # if curr exists
                # append curr left
                # append curr right
                curr = q.popleft()
                if curr:
                    res.append(str(curr.val)) #handle edge case if none
                    q.append(curr.left)
                    q.append(curr.right)
                else:
                    res.append('N')
        # create level order traversal with Nones
        # serialize to str
        s = ','.join(res)
        # return str
        return s
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # str -> level order traversal
        level = data.split(',')
        # build tree from level order traversal
        # init vars
        index = 0
        q = collections.deque()
        root = None if level[0] == 'N' else TreeNode(int(level[0]))
        q.append(root)

        while q:
            for _ in range(len(q)):
                # curr = pop
                curr = q.popleft()
                if curr:
                    # index +=1
                    index +=1
                    # curr.left = index
                    curr.left = None if level[index] == 'N' else TreeNode(int(level[index]))
                    # index +=1
                    index +=1
                    curr.right = None if level[index] == 'N' else TreeNode(int(level[index]))
                    # curr.right = index
                    # add curr left right to q
                    q.append(curr.left)
                    q.append(curr.right)
        # run buildtree
        # return res
        return root
