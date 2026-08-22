class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # two branch recursion
        # define dfs
        def dfs(i, c):
            # base case
            # i oob
            if i == len(profit):
                return 0
            # recursive case
            # skip item i
            skip = dfs(i+1, c)
            # include item i
            include = 0
            if c-weight[i] >= 0:
                include = profit[i] + dfs(i+1, c-weight[i])
            # get max skip and include
            return max(skip, include)
            # return
        # run dfs and return
        return dfs(0, capacity)