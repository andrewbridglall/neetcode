class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        
        queue = collections.deque()
        visit = set()
        
        queue.append([0,0])
        levels = 0
        
        while queue and (R-1, C-1) not in visit:
            qlen = len(queue)
            for i in range(qlen):
                cr, cc = queue.popleft()
                visit.add((cr,cc))
                for dr, dc in directions:
                    if cr+dr < 0 or cc+dc < 0 or \
                    cr+dr >=R or cc+dc >=C or \
                    grid[cr+dr][cc+dc] == 1 or \
                    (cr+dr, cc+dc) in visit:
                        continue
                    queue.append([cr+dr, cc+dc])
            levels +=1
        
        return levels-1 if (R-1, C-1) in visit else -1




        # loop thru queue
        # curr = queue popleft
        # add to visited
        # if curr has valid neighbors -append to queue
        # valid = not oob, not already visited, not 1
        # keep track of level

        
