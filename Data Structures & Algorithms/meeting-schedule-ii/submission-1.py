"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # get all start times
        # get all end times
        # sort arrs
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        # init pointers, vars
        s,e = 0,0
        count = 0
        maxcount = 0
        # while s < len(start)
        # if s < e - another meeting is starting
        # if s >= e - another meeting has ended
        # keep count of overlapping meetings
        # keep track of max count
        while s < len(start):
            if start[s] < end[e]:
                count +=1
                s+=1
            else:
                count -=1
                e +=1
            maxcount = max(maxcount, count)
        # return max
        return maxcount