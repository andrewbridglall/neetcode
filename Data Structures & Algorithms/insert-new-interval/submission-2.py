class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # handle edge case len 0
        # init vars
        res = []
        n = len(intervals)
        # iterate thru intervals
        for i in range(n):
        # compare intervals i to newint
            ns,ne = newInterval
            s,e = intervals[i]
        # 3 cases
            if e < ns:
                res.append(intervals[i])
            elif ne < s:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            else:
                # overlap
                newInterval = [min(s,ns), max(e,ne)]
        # ret res
        res.append(newInterval)
        return res