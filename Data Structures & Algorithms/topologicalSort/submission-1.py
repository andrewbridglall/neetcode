class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(n):
            adj[i] = []
        for u,v in edges:
            adj[u].append(v)

        
        # init ds
        topsort = []
        visit = set()

        # define dfs - postorder traversal
        def dfs(node, path):
            # base case
            if node in path:
                return False
            if node in visit:
                return True
            # recursive case
            visit.add(node)
            path.add(node)
            for neighbor in adj[node]:
                if not dfs(neighbor, path):
                    return False
            topsort.append(node)
            path.remove(node)
            return True

        for i in range(n):
            if not dfs(i, set()):
                return []
        
        topsort.reverse()
        return topsort