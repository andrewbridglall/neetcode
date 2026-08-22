class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # init params
        M,N = len(matrix), len(matrix[0])
        # init ds
        rows = [-1]*(M)
        cols = [-1]*(N)

        # store locations of rows and cols of 0
        for m in range(M):
            for n in range(N):
                if matrix[m][n] == 0:
                    rows[m] = 0
                    cols[n] = 0
        # set vals in matrix if in a zero row or col
        for m in range(M):
            for n in range(N):
                if rows[m] == 0 or cols[n] == 0:
                    matrix[m][n] = 0
        