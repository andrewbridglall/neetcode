class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # bf soln
        # init empty matrix n x n
        n = len(matrix)
        newmatrix = [[0 for _ in range(n)] for _ in range(n)]
        # fill in values based on on src matrix
        # mapping : row 0 -> col n-1 .... row n-1 -> col 0
        # set mtrix to new matrix
        for r in range(n):
            for c in range(n):
                newmatrix[c][n-1-r] = matrix[r][c]

        # copy values back to src matrix
        for r in range(n):
            for c in range(n):
                matrix[r][c] = newmatrix[r][c]
        