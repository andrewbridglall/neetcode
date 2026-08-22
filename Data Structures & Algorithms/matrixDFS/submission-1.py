class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        # init R, C, dirs
        R, C = len(grid), len(grid[0])
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]

        # implement dfs
        def dfs(r,c, visit):
        # base cases
            if r not in range(R) or c not in range(C) or \
            (r,c) in visit or grid[r][c] == 1:
                return 0
            if r == R-1 and c == C-1:
                return 1
            
        # recursive cases
            visit.add((r,c))
            count = 0
            for dr,dc in dirs:
                count += dfs(r+dr, c+dc, visit)
            visit.remove((r,c))
        # return count
            return count
        
        return dfs(0,0, set())