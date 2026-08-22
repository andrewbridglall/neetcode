class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adj list
        adj = defaultdict(list)
        for a,b in prerequisites:
            adj[a].append(b) # a has prerequisite b
        # make dfs
        visit = set()
        
        def dfs(node):
            # base case
            # if node in path - cycle detected ret false
            # if node in visit - already visited ret true
            if node in path:
                return False
            if node in visit:
                return True
            # recursive case
            # add to path
            # add to visit
            path.add(node)
            visit.add(node)
            # go to neighbors
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            path.remove(node)
            return True
        # run dfs on every node. coruses may not be in 1 connected component
        for i in range(numCourses):
            path = set()
            if not dfs(i):
                return False
        return True