class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # strategy - out to in
        # keep track of cells we can make it to from borders
        # store in pac and atl visit sets
        R,C = len(heights), len(heights[0])
        dirs = [[-1,0], [1,0], [0,-1], [0,1]]
        pac, atl = set(), set()

        # run dfs
        def dfs(r,c, visit, prevH):
            # base case
            if (r,c) in visit or r not in range(R) or c not in range(C) or \
                prevH > heights[r][c]:
                return
            # recusrive case
            visit.add((r,c))
            for dr,dc in dirs:
                dfs(r+dr,c+dc, visit, heights[r][c])

        for r in range(R):
            dfs(r,0, pac, heights[r][0])
            dfs(r,C-1, atl, heights[r][C-1])

        for c in range(C):
            # pacific
            dfs(0,c, pac, heights[0][c])
            # atlantic
            dfs(R-1,c, atl, heights[R-1][c])
        
        res = []
        for r in range(R):
            for c in range(C):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res
