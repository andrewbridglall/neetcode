class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # bfs with 8 neighbors instead of 4
        if not grid or grid[0][0] ==1:
            return -1
        
        q = collections.deque()
        visit = set()
        R, C = len(grid), len(grid[0])
        dirs = [[1,0], [-1,0], [0,1], [0,-1],
                [-1,-1], [1,1], [-1,1], [1,-1]]

        q.append((0,0))
        visit.add((0,0)) 

        levels = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                visit.add((r,c))
                if r == R-1 and c == C-1:
                    return levels+1
                # add neighbors
                for dr,dc in dirs:
                    nr,nc = r+dr, c+dc
                    if nr < 0 or nc < 0 or nr >= R or nc >= C or \
                    (nr,nc) in visit or grid[nr][nc] == 1:
                        continue
                    q.append((nr,nc))
                    visit.add((nr,nc))
            levels +=1
        return -1