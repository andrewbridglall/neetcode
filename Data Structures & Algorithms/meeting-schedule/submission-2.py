"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # if intervals empty return true
        if not intervals:
            return True
        # sort based on interval object criteria
        intervals.sort(key=lambda x : x.start)
        # init e1 = intervals 0 end
        e1 = -1
        # compare to intervals 1 ...n
        for i in range(len(intervals)):
            # if overlap - return false
            if e1 > intervals[i].start:
                return False
            else:
                e1 = intervals[i].end
            # if nonoverlap, update e1
        # if overlap - return false
        # return true
        return True
