class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # optimal
        # init vars
        R,C = len(matrix), len(matrix[0])
        zeroList = []
        # iter thru matrix and store pos of 0s
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    zeroList.append((r,c))
        # iterate thru list of pos and set rows cols to 0 only
        for zr,zc in zeroList:
            # set whole zr to 0
            for c in range(C):
                matrix[zr][c] = 0
            # set whole zc to 0
            for r in range(R):
                matrix[r][zc] = 0
        
        