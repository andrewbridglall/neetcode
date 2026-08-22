class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dir = [[1,0], [-1,0], [0,1], [0,-1]]
        maxArea = -1

        def dfs(r,c):
            if r < 0 or c < 0 or r == R or c == C:
                return 0
            if grid[r][c] == 0:
                return 0
            count =1
            grid[r][c] = 0
            for dr, dc in dir:
                count += dfs(r+dr, c+dc)
            return count

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    count = dfs(r,c)
                    maxArea = max(maxArea, count)
        return maxArea if maxArea > 0 else 0