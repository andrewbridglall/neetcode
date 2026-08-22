class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # run dfs
        # caching
        cache = {}

        def dfs(i, amount):
            # base case
            # i oob
            if i == len(coins):
                return sys.maxsize
            # amount == 0
            if amount == 0:
                return 0
            if (i,amount) in cache:
                return cache[(i,amount)]
            # recursive case
            # skip i
            skip = dfs(i+1, amount)
            # include i
            include = sys.maxsize
            if amount - coins[i] >= 0:
                include = 1 + dfs(i, amount - coins[i]) 
            # return min skip incl
            cache[(i,amount)] = min(skip, include) 
            return cache[(i,amount)]

        # return dfs
        res = dfs(0, amount)
        return res if res != sys.maxsize else -1
