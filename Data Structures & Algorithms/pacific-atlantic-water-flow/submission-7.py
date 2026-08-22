class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # init vars
        R,C = len(heights), len(heights[0])
        dirs = [[-1,0], [1,0], [0,-1], [0,1]]
        pacific = set()
        atlantic = set()
        # make dfs
        def dfs(r,c, ocean):
            # base case
            # recursive case
            ocean.add((r,c)) #assume any node we go to is valid
            # go to neigbors
            # only add valid neigbors
            for dr,dc in dirs:
                if r+dr not in range(R) or c+dc not in range(C) or (r+dr, c+dc) in ocean \
                or heights[r][c] > heights[r+dr][c+dc]:
                    continue
                dfs(r+dr,c+dc, ocean)

        # find where pacific water can go
        # starting at first row, first col
        # find where atlantic water can go
        # starting at last row, last col
        for r in range(R):
            dfs(r,0, pacific)
            dfs(r, C-1, atlantic)

        for c in range(C):
            dfs(0,c, pacific)
            dfs(R-1, c, atlantic)

        # return shared points
        res = []
        for r in range(R):
            for c in range(C):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res