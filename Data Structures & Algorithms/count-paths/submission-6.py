class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp soln
        # init vars
        dp = [[0]*(n) for _ in range(m)]
        # base case
        # last row and last col == 1
        for i in range(n):
            dp[m-1][i] = 1
        # run dp from bottom to top
        for r in range(m-2, -1, -1):
            # update val for n-1 == 1
            dp[r][n-1] = 1
            for c in range(n-2, -1, -1):
                dp[r][c] = dp[r+1][c] + dp[r][c+1]

        # return dp 0 0
        return dp[0][0]