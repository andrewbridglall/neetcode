class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = len(intervals)
        # bf
        # make dfs
        def dfs(i, e1):
            # base case
            # handle edge case
            if i == n:
                return 0
            # recursive case
            # include i
            incl = float('inf')
            if e1 <= intervals[i][0]:
                incl = 0 + dfs(i+1, intervals[i][1])
            # skip i
            skip = 1 + dfs(i+1, e1)
            # return min
            return min(incl, skip)
        # run dfs
        return dfs(0, float('-inf'))