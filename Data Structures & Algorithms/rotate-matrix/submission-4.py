class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # init pointers to rows cols
        N = len(matrix)
        # swap elts in place - 4 swaps, go to next item in row/col
        # perform same operation on next layer
        # left right top bot
        left = 0
        right = N-1
        top = 0
        bot = N-1

        while left < right:
            # swaps
            # incr delta 1 - can be +/- as needed
            for i in range(right-left):
                tmp = matrix[top][left+i] # across top row l to r
                matrix[top][left+i] = matrix[bot-i][left] # up left col
                matrix[bot-i][left] = matrix[bot][right-i] # across bot row r to l
                matrix[bot][right-i] = matrix[top+i][right] # down right col
                matrix[top+i][right] = tmp

            # then go to next row/col
            left +=1
            right -=1
            top +=1
            bot -=1