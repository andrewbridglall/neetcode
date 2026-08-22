class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        # init vars
        R,C = len(grid), len(grid[0])
        dirs = [[-1,0], [1,0], [0,1], [0,-1]]
        q = collections.deque()
        visit = set()
        # init q visit
        if grid[0][0] == 0:
            q.append((0,0))
            visit.add((0,0))
        length = 0
        # run bfs
        # while q
        while q:
            # for i in range len q:
            for _ in range(len(q)):
                # curr = popleft
                r,c = q.popleft()
                # if curr == end - return len
                if r == R-1 and c == C-1:
                    return length
                # iterate thru neighbors of curr
                for dr,dc in dirs:
                # append if valid - not oob, not already visited not 1
                # mark neighbors appended as visited
                    if r+dr not in range(R) or c+dc not in range(C) \
                    or (r+dr,c+dc) in visit or grid[r+dr][c+dc] == 1:
                        continue
                    q.append((r+dr,c+dc))
                    visit.add((r+dr,c+dc))
            # incr length
            length +=1

        # return length
        return -1