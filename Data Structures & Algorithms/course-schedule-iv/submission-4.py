class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # build adj
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for a,b in prerequisites:
            adj[b].append(a)
            
        # init vars
        preMap = {i: set() for i in range(numCourses)}
        visit = set()
        # build dfs
        def dfs(i):
            if i in visit:
                return
            visit.add(i)
            for child in adj[i]:
                dfs(child)
                preMap[i].update(preMap[child])
            preMap[i].add(i)
        
        # run dfs on every node
        for i in range(numCourses):
            dfs(i)
        # build hashmap course -> set of prereqs
        # iterate thru queries and append if u in map[v]
        res = []
        for u,v in queries:
            res.append(u in preMap[v])
        # ret res
        return res