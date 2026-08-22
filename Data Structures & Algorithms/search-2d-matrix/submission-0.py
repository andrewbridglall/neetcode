class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == target:
                    return True
        
        return False