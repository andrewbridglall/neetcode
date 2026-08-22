class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # top down memo
        # make cache
        cache = {}
        # make dfs
        def dfs(i, total):
            # base case
            # if total == 0
            if total == 0:
                return 1
            # if i oob
            if i == len(coins):
                return 0
            # if in cache return
            if (i, total) in cache:
                return cache[(i,total)]
            # recursive case
            count = 0
            # skip i
            count += dfs(i+1, total)
            # include i
            if total-coins[i] >= 0:
                count += dfs(i, total-coins[i])
            # return skip + include
            # save res to cache
            cache[(i,total)] = count
            # return res
            return cache[(i,total)]
        # run dfs
        return dfs(0, amount)