class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # start at topleft
        # end at bottomright
        R, C = len(grid), len(grid[0])
        dirs = [[1,0], [-1,0], [0,-1], [0,1]]
        # use minheap to get min of maximums until we reach end
        # init ds
        minheap = []
        visit = set()
        res = 0
        # add first grid pos to minheap
        minheap.append([grid[0][0], 0, 0])
        # run dijkstra's
        # return min max at bottomright
        while minheap:
            # pop from minheap
            height, r, c = heapq.heappop(minheap)
            # if pos already visited - skip
            # add to visit
            # update max
            visit.add((r,c))
            res = height
            if r == R-1 and c == C-1:
                break
            # add neighbors of current to heap
            for dr, dc in dirs:
                # only add if valid
                # only add if not visited already
                if r+dr not in range(R) or c+dc not in range(C) or \
                (r+dr, c+dc) in visit:
                    continue
                heapq.heappush(minheap, [max(height, grid[r+dr][c+dc]), r+dr, c+dc])
        
        # return updated max
        return res
