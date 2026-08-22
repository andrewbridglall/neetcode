class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return -1
        # sort intervals
        intervals.sort()
        # init end to intervals at i 0
        removals = 0
        end = intervals[0][1]
        # iterate thru intervals
        for i in range(1, len(intervals)):
        # if no overlap update end to current interval
            if end <= intervals[i][0]:
                end = intervals[i][1]
        # else (overlap) update end to min end
            else:
                end = min(end, intervals[i][1])
                removals +=1
        # this functionally 'removes' interval from list
        # return count of removals
        return removals