"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # edge case intervals empty
        if not intervals:
            return 0
        # create start end arrs, sort
        start = [i.start for i in intervals]
        end = [i.end for i in intervals]
        start.sort()
        end.sort()
        # while i < len start compare start and end
        maxMeetings = 0
        meetings = 0
        i = j = 0
        while i < len(start):
            if start[i] < end[j]:
                # if start < end - new meeting begun
                meetings +=1
                maxMeetings = max(maxMeetings, meetings)
                i+=1
            else:
                # if end >= start - a meeting ended
                meetings -=1
                j+=1
        # keep count and max
        # return max
        return maxMeetings