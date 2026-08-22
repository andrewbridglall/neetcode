class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # bf
        N, M = len(weight), capacity
        # make dfs
        def dfs(i,cap):
            # base case
            if i == N or cap == 0:
                return 0
            # recursive case
            # incl i
            incl = 0
            if cap-weight[i] >= 0:
                incl = profit[i]+dfs(i+1,cap-weight[i])
            # skip i
            skip = dfs(i+1,cap)
            return max(incl, skip)
        # run dfs
        return dfs(0,capacity)
