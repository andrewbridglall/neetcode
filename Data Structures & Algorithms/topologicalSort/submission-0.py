class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        # build adj list from edges
        adj = {}
        for i in range(n):
            adj[i] = []
        for s,d in edges:
            adj[s].append(d)
        
        # init topsort, visit, path
        topsort, visit, path = [], set(), set()
        for i in range(n):
            if not self.dfs(i, topsort, visit, adj, path):
                print('in here')
                return []
        
        # for every node in n - run dfs - postorder traversal
        # define dfs
        # get to complete topsort
        # reverse topsort
        topsort.reverse()
        return topsort
        # return if no cycles found

    # dfs
    def dfs(self, src, topsort, visit, adj, path):
    # base case
    # if cycle found ret false
    # if src already in ivist -do nothing return
        if src in path:
            return False
        if src in visit:
            return True
    # recusrive case
        visit.add(src)
        path.add(src)
    # run dfs on all neighbors of src
        for neighbor in adj[src]:
            if not self.dfs(neighbor, topsort, visit, adj, path):
                return False
    # add src to topsort at the end -since postorder traversal
    # pop src from path
        topsort.append(src)
        path.remove(src)
        return True
