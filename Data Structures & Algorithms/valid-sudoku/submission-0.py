class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # bf - optimized soln
        # init vars
        # init hashmap of rows cols squares
        sudoku = defaultdict(set)
        n = len(board)
        # iterate thru board
        for r in range(n):
            for c in range(n):
                if board[r][c] == ".":
                    continue
        # check if item already in row col sq
                row, col, sq = "r"+str(r), "c"+str(c), "s"+str((r//3)*3+(c//3))
                if board[r][c] in sudoku[row] or \
                board[r][c] in sudoku[col] or \
                board[r][c] in sudoku[sq]:
                    return False
        # add item to respective row, col, sq
                sudoku[row].add(board[r][c])
                sudoku[col].add(board[r][c])
                sudoku[sq].add(board[r][c])
        # if make it to end ret true
        return True