class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adj
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for a,b in prerequisites:
            adj[a].append(b)
        # init topsort, visit
        topsort = []
        visit = set()

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
            path.remove(node)
            return True

        for i in range(numCourses):
            if not dfs(i, set()):
                return False
        
        return True
        # for every node, run dfs post order 
        # define dfs
        # if cycle detected dfs ret false
        # return true otherwise