class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp soln
        M,N = amount, len(coins)

        # init dp array
        dp = [[0]*(M+1) for _ in range(N+1)]
        # base case amount = 0 top left to bottom right
        for n in range(1, N+1):
            dp[n][0] = 1
            for m in range(1, M+1):
                # incl
                incl = 0
                if m-coins[n-1] >= 0:
                    incl = dp[n][m-coins[n-1]]
                # skip
                skip = dp[n-1][m]
                dp[n][m] = incl + skip
        # return last pos
        return dp[N][M]