class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # optimal dfs soln
        # init vars
        R,C = len(heights), len(heights[0])
        dirs = [[-1,0], [1,0], [0,-1], [0,1]]
        pacific = set()
        atlantic = set()
        # make dfs
        def dfs(r,c,visit,prevHeight):
            # base case
            # if r c already visited or oob return
            if (r,c) in visit or r < 0 or r == R or c < 0 or c == C:
                return
            # recursive case
            # if we made it here, r, c is valid no check
            # compare r c with prevheight
            # if height r c >= prevheight, we can make it to r c
            # add to visit set
            # run dfs on r c neighbors with r c as new prev height
            if heights[r][c] >= prevHeight:
                visit.add((r,c))
                for dr,dc in dirs:
                    dfs(r+dr,c+dc,visit, heights[r][c])

        # find all cells we can visit from pacific
        # first row and first col with prevheight = 0
        # find all cells we can visit from atlantic
        # last row last col with prevheight =0
        
        for r in range(R):
            # pacific is first col
            dfs(r, 0, pacific, 0)
            # atlantic is last col
            dfs(r, C-1, atlantic, 0)

        for c in range(C):
            # pac first row
            dfs(0, c, pacific, 0)
            # atl last row
            dfs(R-1, c, atlantic, 0)

        # check cells common to both sets and return
        res = []
        for r in range(R):
            for c in range(C):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res
        # if cell already visited not visiting again - visiting each cell once per ocean
        # thus time = 2*R*C = RC, space = call stack = longest path - R*C