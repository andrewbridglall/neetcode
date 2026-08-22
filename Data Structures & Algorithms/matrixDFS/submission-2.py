class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        # init vars
        R,C = len(grid), len(grid[0])
        dirs = [[-1,0], [1,0], [0,-1], [0,1]]
        visit = set()
        # make dfs
        def dfs(r,c):
            # base case
            # r c oob, rc visited, [rc] eq 1 - ret 0
            if r not in range(R) or c not in range(C) or (r,c) in visit or grid[r][c] == 1:
                return 0
            # reached end - ret 1
            if r == R-1 and c == C-1:
                return 1
            # recurisve case
            # add rc to visit
            visit.add((r,c))
            # init count -paths to end from rc
            count = 0
            # run dfs up down left right
            for dr,dc in dirs:
                count += dfs(r+dr,c+dc)
            # done processing rc, remove from visit
            visit.remove((r,c))
            # return count
            return count

        # run dfs starting at 0,0
        # return res
        return dfs(0,0)