class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # bf - dfs
        # init vars
        R,C = len(matrix), len(matrix[0])
        dirs = [[-1,0], [1,0], [0,-1], [0,1]]
        visit = set()
        # make dfs
        # remove prev
        # add cache - only use if curr < next
        cache = {}
        def dfs(r,c):
            # base case
            if (r,c) in cache:
                return cache[(r,c)]
            # recursive case
            # r,c is valid
            # add to visit
            # add to length
            # visit.add((r,c))
            maxPath = 1
            # go to neighbors
            for dr, dc in dirs:
                if r+dr not in range(R) or c+dc not in range(C) \
                    or matrix[r][c] >= matrix[r+dr][c+dc]:
                    continue
                maxPath = max(maxPath, 1+dfs(r+dr, c+dc))
            # backtrack and remove from visit
            # visit.remove((r,c))
            # ret max path length from r c
            cache[(r,c)] = maxPath
            return maxPath
        # run dfs for every pos in grid
        for r in range(R):
            for c in range(C):
                dfs(r,c)
        print(cache)
        return max(cache.values())