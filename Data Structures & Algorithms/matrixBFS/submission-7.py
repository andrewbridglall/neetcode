class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        # init queue, visit, len, dirs, rows,cols
        R, C = len(grid), len(grid[0])
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        q = collections.deque()
        visit = set()

        q.append((0,0))
        visit.add((0,0))
        length = 0

        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                if r == R-1 and c == C-1:
                    return length
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if nr not in range(R) or nc not in range(C) or \
                    (nr,nc) in visit or grid[nr][nc] == 1:
                        continue
                    q.append((nr, nc))
                    visit.add((nr, nc))
            length +=1
        return -1
        # while q
        # loop through elts in q
        # pop elt and add neigbors if valid
        # if valid add, if not valid skip
        # incr length
        # check if we reached bottom right