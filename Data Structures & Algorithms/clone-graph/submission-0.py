"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        clone = {} # key = old node, value = new node
        def dfs(old):
            # base cases
            if old in clone:
                return clone[old]
            if old not in clone:
                clone[old] = Node(old.val)
            # recursive caes
            for n in old.neighbors:
                clone[old].neighbors.append(dfs(n))
            return clone[old]
        return dfs(node)

