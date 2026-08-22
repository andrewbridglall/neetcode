class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # build dfs
        def dfs(i, cap):
            # base case
            # if i oob
            if i == len(profit):
                return 0
            # recursive case
            # include item i
            newcap = cap - weight[i]
            include = 0
            if newcap >=0:
                include = profit[i] + dfs(i+1, cap - weight[i])
            # skip item i
            skip = dfs(i+1, cap)
            # return max incl, skip
            return max(include, skip)
        # run dfs
        # ret dfs
        return dfs(0,capacity)