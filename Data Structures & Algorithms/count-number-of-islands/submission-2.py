class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # init vars
        R,C = len(grid), len(grid[0])
        dirs = [[-1,0], [1,0], [0,-1], [0,1]]
        visit = set()
        # make dfs
        def dfs(r,c):
            # base case
            # i oob, viisted, zero return
            if r not in range(R) or c not in range(C) or (r,c) in visit or grid[r][c] == "0":
                return
            # recursive case
            # add rc to visited
            visit.add((r,c))
            # dfs up down left right
            for dr,dc in dirs:
                dfs(r+dr,c+dc)
            

        # for every pos run dfs
        islands = 0
        for r in range(R):
            for c in range(C):
                # if grid pos eq 1 and not visited = new island run dfs
                if grid[r][c] == "1" and (r,c) not in visit:
                    islands +=1
                    dfs(r,c)
        # return res
        return islands