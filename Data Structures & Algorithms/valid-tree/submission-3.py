class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # build adj list
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        visit = set()
        # run dfs
        def dfs(node, parent):
            # base case
            if node in visit:
                return False
            # recursive case
            visit.add(node)
            # run dfs on neighbors
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True
        
        return dfs(0, None) and len(visit) == n