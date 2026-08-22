class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # edge cases
        if not word or not board:
            return False
        # init vars, objs
        R,C = len(board), len(board[0])
        visit = set()
        dirs = [[-1,0], [1,0], [0,-1], [0,1]]

        # run dfs
        def dfs(i,j, k):
            # base case
            # if i j oob, already visited, val neq word k - return false
            if i not in range(R) or j not in range(C) or (i,j) in visit:
                return False
            # if we reached end - word matches and last index -return True
            if board[i][j] == word[k] and k == len(word)-1:
                return True
            # recursive case
            # add grid pos to visit
            visit.add((i,j))
            # if grid i j  == word k - continue with dfs
            if board[i][j] == word[k]:
                # continue dfs
                # go up down left right
                for dr,dc in dirs:
                    if dfs(i+dr, j+dc, k+1):
                        return True
            # pop from visit
            visit.remove((i,j))
            # else return false
            return False

        # run dfs for every pos in grid
        # return dfs
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j, 0):
                    return True
        return False