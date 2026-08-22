class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals
        intervals.sort(key = lambda x: (x[0], x[1]))

        output = []
        newInt = intervals[0]
        # take first and compare to intervals starting at i=1
        for i in range(1, len(intervals)):
            # compare newint to intervals i
            s1,e1 = newInt
            s2,e2 = intervals[i]
            if e1 < s2:
                output.append(newInt)
                newInt = intervals[i]
            else:
                newInt = [min(s1,s2), max(e1,e2)]
        output.append(newInt)

        # return output
        return output