class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        # init q, visit, dirs, r,c
        q, visit = collections.deque(), set()
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        R, C = len(grid), len(grid[0])

        q.append((0,0))
        visit.add((0,0))
        levels = 0

        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                # check if we reached end
                if r == R-1 and c == C-1:
                    return levels

                # add neighbors
                for dr,dc in dirs:
                    nr,nc = r+dr,c+dc
                    if nr not in range(R) or nc not in range(C) or \
                    (nr,nc) in visit or grid[nr][nc] == 1:
                        continue
                    q.append((nr,nc))
                    visit.add((nr,nc))
            levels +=1
            print(levels)
        return -1

        # add start to q, visit
        # while q, iter through q and pop
        # add neigbors if valid
        # increm len at end of for loop
        # if no valid path reutrn -1