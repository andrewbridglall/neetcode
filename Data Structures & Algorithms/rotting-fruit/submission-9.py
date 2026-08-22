class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # init vars
        R,C = len(grid), len(grid[0])
        dirs = [[-1,0], [1,0], [0,-1], [0,1]]
        # make bfs
        # init vars
        q = collections.deque()
        # add all rot fruit to queue
        fresh = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append((r,c))
        # while q
        minutes = 0
        while q:
            for _ in range(len(q)):
                # pop curr
                row,col = q.popleft()
                # add neighbros to q if valid = not oob, not visited, not zero
                for dr,dc in dirs:
                    if row+dr not in range(R) or col+dc not in range(C) or grid[row+dr][col+dc] != 1:
                        continue
                    q.append((row+dr,col+dc))
                    # visit neighbors
                    grid[row+dr][col+dc] = 2
                    fresh -=1
            minutes +=1
        # update level aka minutes
        
        # check if any fresh fruit remain
        # ret levels
        return max(minutes-1,0) if not fresh else -1