class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # run dfs - build soln set
        soln_set = []
        soln = []
        # usedRows = set() # don't need to add to rows since building soln going down
        usedCols = set()
        usedDiagonals = defaultdict(int) # only need to add diagonals going down

        def dfs(i):
            # nonlocal usedDiag
            # base case
            if i == n:
                soln_set.append(soln.copy())
                return
            # recursive case
            # try paths at row i
            for c in range(n):
                # (i,c)
                if c not in usedCols and usedDiagonals[(i,c)] == 0:
                    # if pos valid add to soln
                    soln.append((i,c))
                    # add r, c, diagnals to offlimits
                    usedCols.add(c)
                    # add diag
                    newd = getDiagonals(i,c)
                    # usedDiag |= newd
                    for item in newd:
                        usedDiagonals[item] +=1
                    
                    # go to i+1
                    dfs(i+1)
                    # reset offlimits
                    usedCols.remove(c)
                    # usedDiag -= newd
                    for item in newd:
                        usedDiagonals[item] -=1
                    # remove from soln
                    soln.pop()
        
        def getDiagonals(r,c):
            # given r,c add diagonals going down to set and return
            newDiagonals = set()
            # down and left
            # down and right
            for i in range(1,n):
                if r+i in range(n) and c+i in range(n):
                    newDiagonals.add((r+i,c+i))
                if r+i in range(n) and c-i in range(n):
                    newDiagonals.add((r+i,c-i))
            return newDiagonals
        
        dfs(0)
        # generate boards
        soln_boards = []
        for soln in soln_set:
            # for every soln in soln set generate its board
            newboard = [['.' for _ in range(n)] for _ in range(n)]
            for r,c in soln:
                newboard[r][c] = 'Q'
            soln_boards.append(newboard)
        
        # generate boards matchign output format
        res = []
        for board in soln_boards:
            output_board = []
            # given board
            # join every row into single string and append to new result list
            for r in range(n):
                output_board.append("".join(board[r]))
            res.append(output_board)
        # return
        return res