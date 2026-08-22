class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # bf soln
        # init vars
        intervals.sort()
        n = len(intervals)
        # make dfs
        def dfs(i, e1):
            # base case
            if i == n:
                return 0 # no more intervals to remove
            # recursive case
            s2,e2 = intervals[i]
            # incl i - only including i if does not overlap with prev interval
            incl = n
            if e1 <= s2:
                incl = 0 + dfs(i+1, e2)
            # skip i
            skip = 1 + dfs(i+1, e1)
            # ret min
            return min(incl, skip)
        # run dfs
        # return dfs
        return dfs(0, float('-inf'))