class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp
        n,m = len(coins), amount
        # init dp array
        dp = [[0]*(m+1) for _ in range(n)]
        # fill in first col and row
        for i in range(n):
            dp[i][0] = 1
        for c in range(m+1):
            if c >= coins[0] and c % coins[0] == 0:
                dp[0][c] = 1
        # traverse dp grid
        for i in range(1, n):
            for c in range(1, m+1):
                # skip i
                skip = dp[i-1][c]
                # include i
                include = 0
                if c-coins[i] >= 0:
                    include = dp[i][c-coins[i]]
                # add both
                dp[i][c] = skip+include
        # return last index
        return dp[n-1][m]