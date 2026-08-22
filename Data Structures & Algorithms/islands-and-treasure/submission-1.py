class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # run bfs starting from treasure
        # init vars
        q = collections.deque()
        visit = set()
        R,C = len(grid), len(grid[0])
        dirs = [[-1,0], [1,0], [0,-1], [0,1]]

        # find all treasure and add to queue and visit
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        # run bfs
        d = 0
        while q:
            d +=1
            for _ in range(len(q)):
                # curr = queue popleft
                r,c = q.popleft()
                # add curr neighbors that are valid
                for dr,dc in dirs:
                    if r+dr not in range(R) or c+dc not in range(C) or (r+dr,c+dc) in visit or \
                    grid[r+dr][c+dc] == -1:
                        continue
                    q.append((r+dr, c+dc))
                    # visit neighbors
                    visit.add((r+dr, c+dc))
                    # update grid during bfs
                    grid[r+dr][c+dc] = d