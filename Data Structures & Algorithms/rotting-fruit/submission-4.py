class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # decl queue, visit, fresh
        R, C = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        q = collections.deque()
        visit = set()
        fresh = 0

        # count fresh and rot
        # add all rot to queue
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append((r,c))

        # while q nonempty and fresh >0 continue to run
        minutes = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                visit.add((r,c))
                # add neigbors to q
                for dr,dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr not in range(R) or nc not in range(C) \
                     or (nr,nc) in visit \
                     or grid[nr][nc] != 1:
                        continue
                    # if valid append
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -=1
                        q.append((nr,nc))
            minutes +=1
        return minutes if fresh == 0 else -1
        # if fresh 0 return time, else -1

