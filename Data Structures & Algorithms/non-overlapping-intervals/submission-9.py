class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # implement greedy approach
        # sort
        intervals.sort()
        # init prevEnd and compare to next in intervals
        e1 = intervals[0][1]
        count = 0
        # if no overlap - update prev end to current int
        for i in range(1, len(intervals)):
            s2,e2 = intervals[i]
            if e1 <= s2:
                e1 = e2
            else:
                e1 = min(e1, e2)
                count +=1
        # if overlap - update end to min - so we don't double count overlaps
        return count