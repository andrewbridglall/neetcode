class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # init vars
        output = []
        n = len(intervals)
        # iterate thru intervals
        # three cases - 
        # non overlap new < interval i
        # non overlap i < new
        # overlap - merge
        for i in range(n):
            s,e = intervals[i]
            ns,ne = newInterval
            if e < ns:
                # append i to output
                output.append(intervals[i])
            elif ne < s:
                output.append(newInterval)
                output.extend(intervals[i:])
                return output
            else:
                # overlap
                newInterval = [min(s,ns), max(e,ne)]
            
        output.append(newInterval)
        return output
