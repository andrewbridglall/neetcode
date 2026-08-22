class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # set pointers at 4 corners
        N = len(matrix)
        left,right = 0, N-1
        top, bottom = 0, N-1
        # for all rows in matrix
        # complete entire row - shift pointer and swap
        while left<right:
            for i in range(right-left):
                tmp = matrix[top][left+i]
                matrix[top][left+i] = matrix[bottom-i][left]
                matrix[bottom-i][left] = matrix[bottom][right-i]
                matrix[bottom][right-i] = matrix[top+i][right]
                matrix[top+i][right] = tmp
            left+=1
            right-=1
            top+=1
            bottom -=1
