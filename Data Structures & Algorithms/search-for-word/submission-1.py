class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # init vars
        R, C = len(board), len(board[0])
        visit = set()
        dirs = [[-1,0], [1,0], [0,-1], [0,1]]

        # make dfs
        def dfs(r,c, i):
            # base  case
            # if k == len word - ret true
            if i == len(word):
                return True
            # if row col oob or visited or neq to char - ret false
            if r not in range(R) or c not in range(C) or (r,c) in visit or word[i] != board[r][c]:
                return False
            # recursive case
            visit.add((r,c))
            # go up down left right - ret true if any are true esle false
            for dr, dc in dirs:
                if dfs(r+dr, c+dc, i+1):
                    return True
            visit.remove((r,c))
            return False
        # run dfs
        # run dfs for every pos in grid - if true ret true else false
        # return dfs
        for r in range(R):
            for c in range(C):
                if dfs(r,c,0):
                    return True
        return False