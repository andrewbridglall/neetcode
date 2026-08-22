class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # make adj list
        graph = {i: [] for i in range(numCourses)} # course -> [] list of prereqs
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        visited = set()
        # build dfs
        def dfs(crs):
            if crs in visited:
                return False
            if graph[crs] == []:
                return True
            
            visited.add(crs)
            for pre in graph[crs]:
                if not dfs(pre):
                    return False
            graph[crs] = []
            visited.remove(crs)
            return True

        for n in range(numCourses):
            if not dfs(n):
                return False
        return True