import copy

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # bf
        # init vars
        m,n = len(matrix), len(matrix[0])
        newmatrix = copy.deepcopy(matrix)
        # iter thru matrix and populate newmtrix
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    # set newmatrix row r to 0
                    for j in range(n):
                        newmatrix[r][j] = 0
                    # set newmatrix col c to 0
                    for i in range(m):
                        newmatrix[i][c] = 0
                
                # if matrix r c == 0 - set newmatrix row r col c to 0
                # else r c neq 0 - skip
        # copy newmatrix to matrix
        for r in range(m):
            for c in range(n):
                matrix[r][c] = newmatrix[r][c]
        