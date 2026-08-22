class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # bf
        M,N = amount, len(coins)
        cache = {}
        # make dfs
        def dfs(i, amount):
            # base case
            if amount == 0:
                return 1
            if i == N:
                return 0
            if (i,amount) in cache:
                return cache[(i,amount)]
            # recursive case
            # incl i
            incl = 0
            if amount - coins[i] >= 0:
                incl = dfs(i, amount - coins[i])
            # skip i
            skip = dfs(i+1, amount)
            cache[(i,amount)] = incl + skip
            return incl + skip
        # run dfs
        return dfs(0, amount)