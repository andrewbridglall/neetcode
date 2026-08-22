class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # build adj
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        # make dfs
        visit = set()
        def dfs(node, parent):
            # base case
            if node in visit:
                return False
            # recursive case
            visit.add(node)
            for n in adj[node]:
                if n == parent:
                    continue
                if not dfs(n, node):
                    return False
            return True
            
        # run dfs
        # visit == n
        return dfs(0, -1) and len(visit) == n