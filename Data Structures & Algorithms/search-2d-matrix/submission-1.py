class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #staircase method starting from bottom right
        ROWS, COLS = len(matrix), len(matrix[0])

        r, c = ROWS-1, 0
        while r >= 0 and c < COLS:
            if target > matrix[r][c]:
                c+=1
            elif target < matrix[r][c]:
                r-=1
            else:
                return True
        return False
