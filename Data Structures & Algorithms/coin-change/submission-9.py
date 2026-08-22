class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        # run dfs
        cache = {}
        def dfs(amount):
            # base case
            # amount == 0
            if amount == 0:
                return 0
            # amount < 0
            if amount < 0:
                return float('inf')
            if amount in cache:
                return cache[amount]
            # recursive case
            # try all coins
            numCoins = float('inf')
            for i in range(n):
                numCoins = min(numCoins, 1 + dfs(amount-coins[i]))
            # include coin
            cache[amount] = numCoins
            return cache[amount]
        # ret dfs
        res = dfs(amount)
        return -1 if res == float('inf') else res