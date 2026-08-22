"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # init vars
        # store old new nodes in hashmap
        graph = {}

        # make dfs
        def dfs(node):
            # base case
            # new node already exists - return new node
            if node in graph:
                return graph[node]
            # recursive case
            # build new node from old node
            newNode = Node()
            newNode.val = node.val
            graph[node] = newNode 
            for neighbor in node.neighbors:
                newNode.neighbors.append(dfs(neighbor))
            # run dfs on neighbors and append to neighbors
            # return new node and store in graph
            return newNode
        # run dfs and build new graph absed on old node
        # return res
        return dfs(node) if node else None