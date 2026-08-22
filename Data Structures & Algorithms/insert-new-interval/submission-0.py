class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # cases
        # interval i comes before  newint and no overlap
        # interval i comes after newint and no overlap
        # interval i overlap newint
        res = []
        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            elif newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                res += intervals[i:]
                return res
            else:
                newInterval = [min(newInterval[0], intervals[i][0]),
                                max(newInterval[1], intervals[i][1])]

        res.append(newInterval)
        return res 