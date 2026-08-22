"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort intervals
        intervals.sort(key= lambda i : i.start)
        n = len(intervals)
        # init prevend
        # comparing int1 int2
        # s1 e1
        e1 = -1
        # iterate thru intervals
        for i in range(n):
        # comapre adj intervals
            s2,e2 = intervals[i].start, intervals[i].end
        # if non overlap continue
            if e1 <= s2:
                e1 = e2
        # else overlapping - conflict found ret false
            else:
                return False
        # ret true
        return True
