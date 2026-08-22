class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # init vars
        R, C = len(grid), len(grid[0])
        islands = 0
        # declare dfs
        directions = [(1,0),(-1,0), (0,1), (0,-1)]
        def dfs(r,c):
            if r < 0 or c < 0 or r == R or c == C:
                return
            if grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r+dr, c+dc)

        # loop through grid
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands +=1
        return islands