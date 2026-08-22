class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # implement top sort
        # init vars
        # build adj list
        adj = defaultdict(list)
        for a,b in prerequisites:
            adj[a].append(b) # a has prereq b
        # topsort
        # visit
        visit = set()
        topsort = []
        # make dfs - postorder traversla
        def dfs(node):
            # base case
            # if node already on current path - cycle detected - ret false
            if node in path:
                return False
            # if not on path but in visit - already visited -ret true
            if node in visit:
                return True
            # recursive case
            # add to path, add to viist
            path.add(node)
            # go to neighbors (first) - run dfs
            for n in adj[node]:
                if not dfs(n):
                    return False
            # append current node to topsort
            visit.add(node)
            topsort.append(node)
            # pop from path
            path.remove(node)
            # return true
            return True

        # run dfs for every node - graph may not be conencted
        for i in range(numCourses):
            path = set()
            if not dfs(i):
                return []
        # return topsort if valid else empty list
        return topsort