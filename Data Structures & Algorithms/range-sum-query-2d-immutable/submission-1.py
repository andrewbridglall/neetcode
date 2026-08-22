class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        R, C = len(matrix), len(matrix[0])
        self.newmatrix = [[0]*(C+1) for _ in range(R+1)]

        for r in range(R):
            prefix = 0
            for c in range(C):
                prefix += matrix[r][c]
                above = self.newmatrix[r][c+1]
                self.newmatrix[r+1][c+1] = prefix+above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        lowRight = self.newmatrix[row2+1][col2+1]
        leftCol = self.newmatrix[row2+1][col1+1-1]
        topRow = self.newmatrix[row1+1-1][col2+1]
        topLeft = self.newmatrix[row1+1-1][col1+1-1]
        return lowRight - leftCol - topRow + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)