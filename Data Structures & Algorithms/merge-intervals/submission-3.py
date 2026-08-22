class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # init vars
        intervals.sort()
        res = []
        n = len(intervals)
        insInt = intervals[0]
        # iterate thru intervals 1...n
        for i in range(1, n):
            # two cases
            s,e = intervals[i]
            ns,ne = insInt
            # if insint < int i - add insint to res and update to int i
            if ne < s:
                res.append(insInt)
                insInt = intervals[i]
            # else insint overlaps int i - merge int
            else:
                insInt = [min(s,ns), max(e,ne)]
        # return res
        res.append(insInt)
        return res