"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # greedy
        # store start end times sorted
        n = len(intervals)
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        # i j pointers at each
        i = j = 0
        # keep track of max
        maxcount = 0
        count = 0
        # compare start i end j
        # once we reach end of start, count decreases, so can stop
        while i < n:
        # if start i < end j - new meeting started - incr count
            if start[i] < end[j]:
                count +=1
                maxcount = max(maxcount, count)
                i +=1
        # else end j <= start i - meeting has ended - decr count
            else:
                count -=1
                j +=1

        # return max
        return maxcount