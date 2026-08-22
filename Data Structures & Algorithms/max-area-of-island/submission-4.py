class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # init vars
        R,C = len(grid), len(grid[0])
        dirs = [[-1,0], [1,0], [0,-1], [0,1]]
        # make dfs
        def dfs(r,c):
            # base case
            # r,c oob, visited, 0
            if r not in range(R) or c not in range(C) or grid[r][c] == 0:
                return 0
            # recursrive case
            # grid pos eq 1
            # area eq 1
            area = 1
            grid[r][c] = 0
            # mark visited
            # run dfs up down left right
            for dr,dc in dirs:
                area += dfs(r+dr, c+dc)
            # ret area
            return area

        # at every pos run dfs
        maxarea = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    maxarea = max(maxarea, dfs(r,c))
        # ret res
        return maxarea