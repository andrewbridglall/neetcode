class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # greedy
        # sort int
        intervals.sort()
        n = len(intervals)
        # count total overlapping intervals
        # iter thru intervals
        count = 0
        e1 = float('-inf')
        for i in range(n):
            s2,e2 = intervals[i]
        # if prevEnd <= intervals i - no overlap update prev end to intervals i
            if e1 <= s2:
                e1 = e2
        # else - overlap - set prevend = min prev end intervals i and incr count
            else:
                e1 = min(e1, e2)
                count +=1
        # return count of overlapping ints removed
        return count