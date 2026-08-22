class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n,m = len(coins), amount
        dp = [[sys.maxsize]*(m+1) for _ in range(n)]

        # init first row
        # coins must add up to amount exactly
        dp[0][0] = 0
        for c in range(m+1):
            if c >= coins[0]:
                # we may add coin(s)
                if c % coins[0] == 0:
                    dp[0][c] = c//coins[0]

        # iterate row by row through dp grid
        for i in range(1, n):
            for c in range(m+1):
                # skip i
                skip = dp[i-1][c]
                # include i
                include = sys.maxsize
                if c-coins[i] >= 0:
                    include = 1 + dp[i][c-coins[i]]
                # take min
                dp[i][c] = min(skip, include)
        # return dp n-1 m
        res = dp[n-1][m]
        return res if res != sys.maxsize else -1