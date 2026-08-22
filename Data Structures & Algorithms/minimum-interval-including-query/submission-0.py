class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # bf
        
        # init vars
        n = len(intervals)
        m = len(queries)
        output = [0]*m
        # optimize by sorting intervals first
        # if intervals sorted, once we arrive at left index > query, we can stop
        intervals.sort()
        # for every query
        for i in range(m):
            query = queries[i]
            shortestInt = float('inf')
        # iterate thru all intervals and check which has shortest int
            for j in range(n):
                left, right = intervals[j]
                if query > right:
                    continue
                elif left <= query <= right:
                    # valid
                    shortestInt = min(shortestInt, right-left+1)                    
                elif query < left:
                    break
            output[i] = -1 if shortestInt == float('inf') else shortestInt
        # ret output
        return output