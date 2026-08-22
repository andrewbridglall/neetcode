class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # init params
        M,N = len(matrix), len(matrix[0])
        # init ds
        # now, overlay rows, cols of zeros on matrix itself
        rowZero = -1

        # store locations of rows and cols of 0
        for m in range(M):
            for n in range(N):
                if matrix[m][n] == 0:
                    if m == 0:
                        rowZero = 0
                    else:
                        matrix[m][0] = 0
                    matrix[0][n] = 0
        # set vals in matrix if in a zero row or col - starting from row 1, col 1
        for m in range(1, M):
            for n in range(1, N):
                if matrix[m][0] == 0 or matrix[0][n] == 0:
                    matrix[m][n] = 0
        
        if matrix[0][0] == 0:
            for m in range(M):
                matrix[m][0] = 0

        if rowZero == 0:
            for n in range(N):
                matrix[0][n] = 0        