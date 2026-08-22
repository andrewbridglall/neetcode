class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # implement topsort
        
        # build adj
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for a,b in prerequisites:
            adj[a].append(b)
        # declare topsort, visit
        topsort = []
        visit = set()

        # define dfs - postorder traversal
        def dfs(node, path):
            # base case
            if node in path:
                return False
            if node in visit:
                return True
            path.add(node)
            visit.add(node)
            # recursive case
            # traverse childen
            for neighbor in adj[node]:
                if not dfs(neighbor, path):
                    return False
            # append root
            topsort.append(node)
            path.remove(node)
            return True


        # run dfs for every node in graph
        for i in range(numCourses):
            if not dfs(i, set()):
                return []
        # if dfs ret false - ret []

        # reverse topsort
        # return topsort
        # topsort.reverse()
        return topsort