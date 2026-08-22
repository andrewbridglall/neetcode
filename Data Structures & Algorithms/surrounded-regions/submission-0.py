class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # init vars
        N,M = len(board), len(board[0])
        dirs = [[-1,0], [1,0], [0,-1], [0,1]]
        queue = collections.deque()
        visit = set()
        # find all zeroes on borders
        # row 0, col 0, row n-1, col n-1
        # add to queue and visited
        for c in range(M):
            if board[0][c] == 'O':
                queue.append((0,c))
                visit.add((0,c))
            if board[N-1][c] == 'O':
                queue.append((N-1, c))
                visit.add((N-1, c))
        for r in range(N):
            if board[r][0] == 'O':
                queue.append((r,0))
                visit.add((r,0))
            if board[r][M-1] == 'O':
                queue.append((r,M-1))
                visit.add((r,M-1))

        # make bfs to find all connected 0s
        # while queue
        def bfs():
            while queue:
            # for _ in range len q
                for _ in range(len(queue)):
                # n,m = popleft  from q
                    n,m = queue.popleft()
                # go to neighbors
                    for dr,dc in dirs:
                        # check if valid
                        # add neighbors if neighbor not oob, not already visited, not an X
                        if n+dr not in range(N) or m+dc not in range(M) or (n+dr, m+dc) in visit \
                        or board[n+dr][m+dc] == 'X':
                            continue
                        # add if O and visit
                        queue.append((n+dr,m+dc))
                        visit.add((n+dr,m+dc))
        # run bfs
        bfs()
        # iterate thru board - if r,c in visit do not modify all else X's
        # viist stores all O's connected to border Os - not surrounded everything else can be X
        for n in range(N):
            for m in range(M):
                if (n,m) in visit or board[n][m] == 'X':
                    continue
                board[n][m] = 'X'
        
          