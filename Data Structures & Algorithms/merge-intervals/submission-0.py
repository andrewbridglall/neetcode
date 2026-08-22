class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals
        intervals.sort(key= lambda i: i[0])
        # init vars
        res = []
        currInt = intervals[0]
        i = 1
        # while loop
        while i < len(intervals):
            # if currInt not overlapping intervals i
            if currInt[1] < intervals[i][0]:
            # append currint to res and update currint to i
                res.append(currInt)
                currInt = intervals[i]
            # else currInt overlaps itnerval i
            else:
            # merge currint and interval i and update currint
                currInt = [min(currInt[0], intervals[i][0]),
                            max(currInt[1], intervals[i][1])]
            # next interval i+1
            i+=1

        # append currinterval
        res.append(currInt)
        # return
        return res