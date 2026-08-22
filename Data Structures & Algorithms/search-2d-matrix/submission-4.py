class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS-1

        midrow = None
        while top <= bot:
            midrow = (top+bot)//2
            if target > matrix[midrow][-1]:
                top = midrow+1
            elif target < matrix[midrow][0]:
                bot = midrow-1
            else:
                break
        
        if top > bot:
            return False
        
        l, r = 0, COLS-1
        while l <= r:
            m = (l+r)//2
            if target > matrix[midrow][m]:
                l = m+1
            elif target < matrix[midrow][m]:
                r = m-1
            else:
                return True
        
        return False
