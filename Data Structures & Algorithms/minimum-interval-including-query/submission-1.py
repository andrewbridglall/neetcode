class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # minheap soln
        # init vars
        n = len(intervals)
        m = len(queries)
        # sort intervals 
        intervals.sort()
        # sort queries and store copy
        sortedQueries = sorted(queries)
        # iterate through queries
        i = 0 # pointer to intervals
        minheap = []
        qmap = defaultdict(int)
        for query in sortedQueries:
        # keep pointer in intervals and add interval to minheap st. left <= query
        # update pointer
            while i < n:
                left, right = intervals[i]
                if left <= query:
                    heapq.heappush(minheap, [right-left+1, left, right])
                    i +=1
                else:
                    break
        # check if top minheap is valid interval = store result in query map, else pop from minheap
            while minheap:
                # top represents shortest interval
                # check that interval is valid ie, left <= query <= right
                length, left, right = minheap[0]
                if left <= query <= right:
                    qmap[query] = length
                    break
                else:
                    heapq.heappop(minheap)
        # if minheap empty store -1 - no matching interval
            if not minheap:
                qmap[query] = -1
        # done when iterated through all queries and intervals
        # build output by iter thru original queries and append result
        output = []
        for q in queries:
            output.append(qmap[q])
        # ret output
        return output