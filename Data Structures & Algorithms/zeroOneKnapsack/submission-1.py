class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # build dfs
        # memoization soln
        n, m = len(profit), capacity
        cache = [[-1]*(m+1) for _ in range(n)]
        
        def memo(i, cap, cache):
            # base case
            # if i oob
            if i == len(profit):
                return 0
            if cache[i][cap] != -1:
                return cache[i][cap]
            # recursive case
            # include item i
            newcap = cap - weight[i]
            include = 0
            if newcap >=0:
                include = profit[i] + memo(i+1, cap - weight[i], cache)
            # skip item i
            skip = memo(i+1, cap, cache)
            # return max incl, skip
            cache[i][cap] = max(include, skip)
            return cache[i][cap]
        # run dfs
        # ret dfs
        return memo(0,capacity, cache)