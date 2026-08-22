class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # approach as unbounded knapsack
        n = len(coins)
        cache = {}
        # make dfs
        def dfs(i, amount):
            # base case
            if amount == 0:
                return 0
            if (i,amount) in cache:
                return cache[(i,amount)]
            # recursive case
            # include i
            incl = skip = float('inf')
            if amount-coins[i] >= 0:
                incl = 1+dfs(i, amount-coins[i])
            # skip i
            if i+1 < n:
                skip = dfs(i+1, amount)
            # ret min
            
            cache[(i,amount)] = min(incl, skip)
            return cache[(i,amount)]
        # run dfs
        res = dfs(0,amount)
        return -1 if res == float('inf') else res