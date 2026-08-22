class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # init vars
        N = len(grid)
        visit = set()
        dirs = [[-1,0], [1,0], [0,-1], [0,1]]
        maxTime = float('-inf')
        minheap = []
        heapq.heappush(minheap, [grid[0][0], 0,0])
        
        # run dijkstra's
        while minheap:
            # pop from heap
            elv, r, c = heapq.heappop(minheap)
            if (r,c) in visit:
                continue
            # update max
            visit.add((r,c))
            maxTime = max(maxTime, elv)
            # edge cases
            if r == N-1 and c == N-1:
                return maxTime
            # add neighbors
            for dr,dc in dirs:
                if r+dr not in range(N) or c+dc not in range(N) or (r+dr,c+dc) in visit:
                    continue
                heapq.heappush(minheap, [grid[r+dr][c+dc], r+dr, c+dc])
        # return max along min path
        return -1
